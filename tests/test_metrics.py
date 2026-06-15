from app import metrics
from app.metrics import percentile


def reset_metrics() -> None:
    metrics.REQUEST_LATENCIES.clear()
    metrics.REQUEST_COSTS.clear()
    metrics.REQUEST_TOKENS_IN.clear()
    metrics.REQUEST_TOKENS_OUT.clear()
    metrics.QUALITY_SCORES.clear()
    metrics.ERRORS.clear()
    metrics.TRAFFIC = 0


def test_percentile_basic() -> None:
    assert percentile([100, 200, 300, 400], 50) >= 100


def test_snapshot_error_rate() -> None:
    reset_metrics()
    try:
        metrics.record_request(
            latency_ms=100,
            cost_usd=0.01,
            tokens_in=10,
            tokens_out=20,
            quality_score=0.8,
        )
        metrics.record_error("RuntimeError")

        snapshot = metrics.snapshot()

        assert snapshot["traffic"] == 1
        assert snapshot["error_count"] == 1
        assert snapshot["error_rate_pct"] == 50.0
    finally:
        reset_metrics()
