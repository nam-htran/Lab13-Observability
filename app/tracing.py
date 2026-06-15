from __future__ import annotations

import os
from typing import Any

try:
    from langfuse import get_client, observe
except Exception:  # pragma: no cover
    def observe(*args: Any, **kwargs: Any):
        def decorator(func):
            return func

        return decorator

    def get_client(*args: Any, **kwargs: Any):
        return None


class _LangfuseContext:
    def update_current_trace(self, **kwargs: Any) -> None:
        client = get_client()
        if client is not None:
            client.update_current_trace(**kwargs)

    def update_current_observation(self, **kwargs: Any) -> None:
        client = get_client()
        if client is None:
            return

        metadata = kwargs.pop("metadata", None)
        usage_details = kwargs.pop("usage_details", None)
        generation_fields = {"model", "model_parameters", "cost_details", "prompt"}
        if usage_details or generation_fields.intersection(kwargs):
            client.update_current_generation(
                metadata=metadata,
                usage_details=usage_details,
                **kwargs,
            )
        else:
            client.update_current_span(metadata=metadata, **kwargs)

    def flush(self) -> None:
        client = get_client()
        if client is not None:
            client.flush()


langfuse_context = _LangfuseContext()


def tracing_enabled() -> bool:
    return bool(os.getenv("LANGFUSE_PUBLIC_KEY") and os.getenv("LANGFUSE_SECRET_KEY"))


def flush_traces() -> None:
    if tracing_enabled():
        try:
            langfuse_context.flush()
        except Exception:
            return None
