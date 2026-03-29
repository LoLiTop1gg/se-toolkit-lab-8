# Observability Skill

Use this skill when the user asks about errors, logs, traces, system health, or "what went wrong".

## Tools available
- `mcp_obs_logs_search` — search logs with LogsQL
- `mcp_obs_logs_error_count` — count errors for a service
- `mcp_obs_traces_list` — list recent traces for a service
- `mcp_obs_traces_get` — get full span details for a trace

## Investigation flow for "What went wrong?" or "Check system health"

Always follow this exact sequence:
1. Call `mcp_obs_logs_error_count` with service="Learning Management Service" and time_window="10m"
2. Call `mcp_obs_logs_search` with query `_time:10m service.name:"Learning Management Service" severity:ERROR` to get recent error details and extract trace_id
3. Call `mcp_obs_traces_get` with the most recent trace_id found in step 2
4. Summarize in plain language — mention BOTH log evidence AND trace evidence, name the affected service and the root failing operation. Do NOT dump raw JSON.

## Summary format
- Which service failed
- What the log shows (event name, severity)
- What the trace shows (which span failed, what error)
- What the HTTP response was (status code)

## Service names
- LMS backend: `Learning Management Service`

## Important
- Always use fresh recent time windows (10m or less)
- The backend may misreport real database failures as 404 — check traces for the real root cause
- Cite both log evidence and trace evidence in every investigation summary
