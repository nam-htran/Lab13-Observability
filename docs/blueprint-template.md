# Day 13 Observability Lab Report

> **Instruction**: Fill in all sections below. This report is designed to be parsed by an automated grading assistant. Ensure all tags (e.g., `[GROUP_NAME]`) are preserved.

## 1. Team Metadata
- [GROUP_NAME]: Individual Submission - 2A202600870 - Trần Hoàng Nam
- [REPO_URL]: https://github.com/nam-htran/Lab13-Observability
- [MEMBERS]:
  - 2A202600870 - Trần Hoàng Nam | Role: Logging, PII, Tracing, SLO, Alerts, Load Test, Dashboard, Demo & Report

---

## 2. Group Performance (Auto-Verified)
- [VALIDATE_LOGS_FINAL_SCORE]: 100/100
- [TOTAL_TRACES_COUNT]: 11 traces verified in Langfuse API
- [PII_LEAKS_FOUND]: 0

---

## 3. Technical Evidence (Group)

### 3.1 Logging & Tracing
- [EVIDENCE_CORRELATION_ID_SCREENSHOT]: docs/evidence/correlation-id-log.png
- [EVIDENCE_PII_REDACTION_SCREENSHOT]: docs/evidence/pii-redaction-log.png
- [EVIDENCE_TRACE_WATERFALL_SCREENSHOT]: docs/evidence/langfuse-trace-waterfall.png
- [TRACE_WATERFALL_EXPLANATION]: A `/chat` request creates one Langfuse trace named `run`; inside it, `rag_retrieve` shows retrieval latency and `llm_generate` is recorded as a generation span with token usage. This makes it possible to separate retrieval latency, model generation, total request latency, and cost.

### 3.2 Dashboard & SLOs
- [DASHBOARD_6_PANELS_SCREENSHOT]: docs/evidence/dashboard-6-panels.png
- [SLO_TABLE]:
| SLI | Target | Window | Current Value |
|---|---:|---|---:|
| Latency P95 | < 3000ms | 28d | ~151ms during normal load test |
| Error Rate | < 2% | 28d | 0% |
| Cost Budget | < $2.5/day | 1d | ~$0.02 for sample load test |

### 3.3 Alerts & Runbook
- [ALERT_RULES_SCREENSHOT]: docs/evidence/alert-rules.png
- [SAMPLE_RUNBOOK_LINK]: docs/alerts.md#1-high-latency-p95

---

## 4. Incident Response (Group)
- [SCENARIO_NAME]: rag_slow
- [SYMPTOMS_OBSERVED]: P95 latency increased and several requests became slow when the `rag_slow` incident toggle was enabled.
- [ROOT_CAUSE_PROVED_BY]: Langfuse trace waterfall shows the retrieval step `rag_retrieve` taking longer, while logs keep the same `correlation_id` across `request_received` and `response_sent`. Metrics also expose increased `latency_p95`.
- [FIX_ACTION]: Disable the `rag_slow` incident toggle and use the alert runbook to isolate the slow retrieval layer.
- [PREVENTIVE_MEASURE]: Keep the `high_latency_p95` alert, inspect slow traces first, and add a fallback retrieval source or timeout for the RAG step.

---

## 5. Individual Contributions & Evidence

### [MEMBER_A_NAME]: 2A202600870 - Trần Hoàng Nam
- [TASKS_COMPLETED]: Implemented correlation ID middleware, structured JSON logging, request context enrichment, recursive PII scrubbing, Langfuse v3 tracing, RAG/LLM spans, metrics export, alert configuration, load test support, validation tests, and this report draft.
- [EVIDENCE_LINK]: https://github.com/nam-htran/Lab13-Observability/commit/c8d3f31 and https://github.com/nam-htran/Lab13-Observability/commit/e3a5cbc

---

## 6. Bonus Items (Optional)
- [BONUS_COST_OPTIMIZATION]: Cost metrics are exported through `/metrics` (`avg_cost_usd`, `total_cost_usd`, tokens in/out) and can be monitored with the `cost_budget_spike` alert.
- [BONUS_AUDIT_LOGS]: Not implemented.
- [BONUS_CUSTOM_METRIC]: Added `error_count` and `error_rate_pct` to `/metrics` for dashboard and alert use.
