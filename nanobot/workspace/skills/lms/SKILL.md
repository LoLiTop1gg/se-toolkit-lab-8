---
name: lms
description: Use LMS MCP tools for live course data
always: true
---

## Available tools
- `lms_health` — check backend health and item count
- `lms_labs` — list all available labs
- `lms_pass_rates` — get pass rates for a specific lab
- `lms_scores` — get score distribution for a specific lab
- `lms_groups` — get group performance for a specific lab
- `lms_timeline` — get submission timeline for a specific lab
- `lms_top_learners` — get top learners for a specific lab

## Strategy
- If the user asks about scores, pass rates, completion, groups, timeline, or top learners without naming a lab — call `lms_labs` first
- If multiple labs are available, ask the user to choose one
- Use each lab title as the user-facing label
- Let the shared `structured-ui` skill decide how to present choices on supported channels

## Formatting
- Show percentages with one decimal place (e.g. 73.5%)
- Show counts as whole numbers
- Keep responses concise

## When asked "what can you do?"
Explain that you can query live LMS data: list labs, show pass rates, scores, group performance, submission timelines, and top learners.
