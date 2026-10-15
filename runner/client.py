"""Async OpenRouter client (OpenAI-compatible endpoint).

One shared AsyncOpenAI client; concurrency is bounded by a semaphore at the
call sites (the Parallel.ForEachAsync equivalent). Retries with exponential
backoff on transient errors / 429s, honouring Retry-After when present.
"""
from __future__ import annotations

import asyncio
import random
import time
from dataclasses import dataclass

from .config import Config


@dataclass
class Completion:
    text: str
    model_returned: str
    prompt_tokens: int | None
    completion_tokens: int | None
    latency_s: float
    attempts: int


class Client:
    def __init__(self, cfg: Config):
        # Imported lazily so selftest/dry-run work without the SDK installed.
        import os

        from openai import AsyncOpenAI

        try:
            import httpx
        except ImportError:  # some environments ship the httpx2 fork instead
            import httpx2 as httpx

        self.cfg = cfg
        # Build the HTTP client explicitly with trust_env=False: the sandbox's
        # NO_PROXY list contains bracketed IPv6 entries that httpx's proxy
        # pattern parser chokes on ("Invalid port: ':1]'"). We pass the proxy
        # URL through ourselves when one is configured.
        proxy = (
            os.environ.get("HTTPS_PROXY")
            or os.environ.get("https_proxy")
            or os.environ.get("ALL_PROXY")
            or os.environ.get("all_proxy")
        )
        http_client = httpx.AsyncClient(
            proxy=proxy,
            trust_env=False,
            timeout=cfg.request_timeout_s,
        )
        self._client = AsyncOpenAI(
            base_url=cfg.base_url,
            api_key=cfg.api_key(),
            timeout=cfg.request_timeout_s,
            max_retries=0,  # we do our own backoff so attempts are countable
            http_client=http_client,
        )

    async def complete(
        self,
        model: str,
        messages: list[dict],
        max_tokens: int,
        temperature: float | None = None,
        reasoning_effort: str | None = None,
    ) -> Completion:
        last_exc: Exception | None = None
        use_reasoning = reasoning_effort
        use_max_tokens = max_tokens
        for attempt in range(1, self.cfg.max_attempts + 1):
            start = time.monotonic()
            try:
                kwargs: dict = {}
                if use_reasoning:
                    kwargs["extra_body"] = {"reasoning": {"effort": use_reasoning}}
                resp = await self._client.chat.completions.create(
                    model=model,
                    messages=messages,
                    max_tokens=use_max_tokens,
                    temperature=self.cfg.temperature if temperature is None else temperature,
                    **kwargs,
                )
                latency = time.monotonic() - start
                choice = resp.choices[0]
                usage = getattr(resp, "usage", None)
                text = (choice.message.content or "").strip()
                if not text and attempt < self.cfg.max_attempts:
                    # Reasoning models can burn the whole token budget on
                    # hidden reasoning and return empty content; retry.
                    await asyncio.sleep(1.0)
                    continue
                return Completion(
                    text=text,
                    model_returned=getattr(resp, "model", model),
                    prompt_tokens=getattr(usage, "prompt_tokens", None),
                    completion_tokens=getattr(usage, "completion_tokens", None),
                    latency_s=round(latency, 3),
                    attempts=attempt,
                )
            except Exception as e:  # noqa: BLE001 - classify below
                last_exc = e
                status = getattr(e, "status_code", None) or getattr(
                    getattr(e, "response", None), "status_code", None
                )
                if status == 400 and use_reasoning:
                    # Provider rejected the reasoning parameter; drop it and
                    # retry rather than failing the call.
                    print(f"  note: {model} rejected reasoning effort "
                          f"{use_reasoning!r}; continuing without it")
                    use_reasoning = None
                    continue
                if status == 400 and use_max_tokens > 8000:
                    # Provider's max output is below our requested cap; halve
                    # and retry rather than failing the call.
                    use_max_tokens //= 2
                    print(f"  note: {model} rejected max_tokens; "
                          f"retrying with {use_max_tokens}")
                    continue
                transient = status is None or status in (408, 409, 425, 429) or status >= 500
                if not transient or attempt == self.cfg.max_attempts:
                    raise
                delay = min(60.0, 2.0 ** attempt) + random.uniform(0, 1.0)
                retry_after = None
                resp_obj = getattr(e, "response", None)
                if resp_obj is not None:
                    headers = getattr(resp_obj, "headers", {}) or {}
                    retry_after = headers.get("retry-after") or headers.get("Retry-After")
                if retry_after:
                    try:
                        delay = max(delay, float(retry_after))
                    except ValueError:
                        pass
                await asyncio.sleep(delay)
        raise RuntimeError(f"Completion failed after retries: {last_exc}")
