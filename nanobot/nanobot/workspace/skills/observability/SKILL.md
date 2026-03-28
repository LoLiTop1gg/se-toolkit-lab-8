# Observability Skill

Use this skill when the user asks about errors, logs, traces, or system health.

## Tools available
- `obs_logs_search` — search logs with LogsQL
- `obs_logs_error_count` — count errors for a service
- `obs_traces_list` — list recent traces for a service
- `obs_traces_get` — get full span details for a trace

## Reasoning flow

1. When asked about errors: call `obs_logs_error_count` first with service="Learning Management Service" and appropriate time_window (e.g. "10m")
2. If errors found: call `obs_logs_search` to get details and extract trace_id values
3. If trace_id found: call `obs_traces_get` to inspect the failing span
4. Summarize findings concisely — do NOT dump raw JSON, describe what failed and where

## Service names
- LMS backend: `Learning Management Service`

## Example queries
- "Any errors in the last 10 minutes?" → logs_error_count + logs_search
- "What went wrong?" → logs_search with severity:ERROR + traces_get
