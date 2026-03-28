# Lab 8 — Report

Paste your checkpoint evidence below. Add screenshots as image files in the repo and reference them with `![description](path)`.

## Task 1A — Bare agent
### What is the agentic loop?
The agentic loop is the fundamental cycle that an AI agent follows to accomplish tasks autonomously. It typically consists of these core stages:
 1 Perceive — Gather information from the environment (user input, tool outputs, files, APIs, etc.)
 2 Reason/Plan — Analyze the information, determine goals, and decide on the next action(s)
 3 Act — Execute actions using available tools (file operations, web searches, code execution, API calls, etc.)
 4 Observe — Receive feedback from the action's outcome
 5 Repeat — Continue the loop until the goal is achieved or a stopping condition is met
### What labs are available in our LMS?
Based on my exploration of the LMS (Learning Management System) workspace, here are the available labs:
Required Labs
Located in /lab/tasks/required/:
 • Task 1 — Set Up the Agent
 • Task 2 — Deploy the Agent and Add a Web Client
 • Task 3 — Give the Agent New Eyes (Observability)
 • Task 4 — Diagnose a Failure and Make the Agent Proactive
Optional Labs
Located in /lab/tasks/optional/:
 • Task 1 — (Optional task)
Lab Documentation
There's also wiki documentation for labs at:
 • /wiki/lab-1/ — Lab 1 documentation
 • /wiki/lab.md — General lab instructions and setup guide
The current lab you're working on is Lab 8 (based on the repository name se-toolkit-lab-8), which focuses on building an AI agent using the nanobot framework with:
 • MCP (Model Context Protocol) tools for LMS backend access
 • WebSocket channel for web client connectivity
 • Flutter web chat interface
 • Observability tools (VictoriaLogs, VictoriaTraces)
 • Proactive health monitoring with cron так?

## Task 1B — Agent with LMS tools
Here are the available labs:
 1 Lab 01 – Products, Architecture & Roles
 2 Lab 02 — Run, Fix, and Deploy a Backend Service
 3 Lab 03 — Backend API: Explore, Debug, Implement, Deploy
 4 Lab 04 — Testing, Front-end, and AI Agents
 5 Lab 05 — Data Pipeline and Analytics Dashboard
 6 Lab 06 — Build Your Own Agent
 7 Lab 07 — Build a Client with an AI Coding Agent
 8 lab-08 
Lab     Completion Rate  Passed  Total 
 ────────────────────────────────────── 
 Lab 01  100.0%           258     258   
 Lab 02  89.1%            131     147   
 Lab 03  89.1%            156     175   
 Lab 04  96.7%            238     246   
 Lab 05  98.4%            246     250   
 Lab 06  98.4%            241     245   
 Lab 07  99.6%            236     237   
 Lab 08  0.0%             0       0     
Lab 08 has the lowest pass rate at 0.0%, but this appears to be because no students have attempted it yet (0 total).

��� nanobot
Yes, the LMS backend is healthy. It currently has 56 items.��� nanobot
## Task 1C — Skill prompt
Which lab would you like to see the scores for? Here are the available labs:

 1 Lab 01 – Products, Architecture & Roles
 2 Lab 02 — Run, Fix, and Deploy a Backend Service
 3 Lab 03 — Backend API: Explore, Debug, Implement, Deploy
 4 Lab 04 — Testing, Front-end, and AI Agents
 5 Lab 05 — Data Pipeline and Analytics Dashboard
 6 Lab 06 — Build Your Own Agent
 7 Lab 07 — Build a Client with an AI Coding Agent
 8 lab-08

Please let me know which lab you'd like to see the score distribution for.
## Task 2A — Deployed agent

| Using config: /app/nanobot/config.resolved.json
nanobot-1  | Using config: /app/nanobot/config.resolved.json
nanobot-1  | ��� Starting nanobot gateway version 0.1.4.post5 on port 18790...
nanobot-1  | 2026-03-28 10:27:51.102 | DEBUG    | nanobot.channels.registry:discover_all:64 - Skipping built-in channel 'matrix': Matrix dependencies not installed. Run: pip install nanobot-ai[matrix]
nanobot-1  | Warning: No channels enabled
nanobot-1  | ✓ Heartbeat: every 1800s
...
## Task 2B — Web client

What can you do in this system?
I'm nanobot ���, your AI assistant! Here's what I can do in this system:

## Core Capabilities

**File & System Operations**
- Read, write, and edit files
- List directory contents
- Execute shell commands (with safety limits)

**Web & Information**
- Search the web
- Fetch and extract content from URLs
- Send messages with file attachments (images, documents, audio, video)

**Task Management**
- Schedule reminders and recurring tasks
- Spawn subagents for complex or time-consuming tasks
- Maintain long-term memory and history logs

## Specialized Skills

**LMS Integration** — Query live learning management system data:
- List available labs
- Show pass rates, scores, and completion rates
- View group performance and submission timelines
- Get top learners per lab

**Interactive UI** — Present choices and confirmations on supported chat channels

**Skill Registry** — Search and install new skills from ClawHub

**Built-in Skills Available:**
- `cron` — Schedule reminders
- `memory` — Two-layer memory system
- `clawhub` — Install public skills
- `skill-creator` — Create custom skills
- `structured-ui` — Interactive messages
- `lms` — Learning management queries

Some skills (weather, github, summarize, tmux) need dependencies installed first.

Is there something specific you'd like help with?

What tools do you have right now?
Based on my current system, here are the tools I have available:

## File & System Tools
| Tool | Purpose |
|------|---------|
| `read_file` | Read file contents (with pagination) |
| `write_file` | Write content to files |
| `edit_file` | Find and replace text in files |
| `list_dir` | List directory contents |
| `exec` | Execute shell commands |

## Web Tools
| Tool | Purpose |
|------|---------|
| `web_search` | Search the web (1-10 results) |
| `web_fetch` | Fetch URL and extract readable content |

## Communication Tools
| Tool | Purpose |
|------|---------|
| `message` | Send messages with file attachments to chat channels |
| `mcp_webchat_ui_message` | Send interactive UI payloads (choices, confirmations) to WebChat |

## Task & Scheduling Tools
| Tool | Purpose |
|------|---------|
| `cron` | Schedule reminders and recurring tasks |
| `spawn` | Spawn subagents for background tasks |

## LMS (Learning Management System) Tools
| Tool | Purpose |
|------|---------|
| `mcp_lms_lms_health` | Check LMS backend health |
| `mcp_lms_lms_labs` | List all available labs |
| `mcp_lms_lms_learners` | List all registered learners |
| `mcp_lms_lms_pass_rates` | Get pass rates for a lab |
| `mcp_lms_lms_timeline` | Get submission timeline for a lab |
| `mcp_lms_lms_groups` | Get group performance for a lab |
| `mcp_lms_lms_top_learners` | Get top learners for a lab |
| `mcp_lms_lms_completion_rate` | Get completion rate for a lab |
| `mcp_lms_lms_sync_pipeline` | Trigger LMS sync pipeline |

Since you're on **WebChat**, I can also send you interactive UI elements like choice buttons and confirmation dialogs using the `mcp_webchat_ui_message` tool.

Anything specific you'd like me to help with?

How is the backend doing?
The LMS backend is **healthy** ✅

- **Status**: Healthy
- **Item Count**: 56 items
- **Errors**: None

Everything looks good! Is there anything specific you'd like to check or do with the LMS data?

Show me the scores
The interactive UI isn't available right now. Here are the available labs — please tell me which one you'd like to see scores for:

1. **Lab 01** – Products, Architecture & Roles
2. **Lab 02** — Run, Fix, and Deploy a Backend Service
3. **Lab 03** — Backend API: Explore, Debug, Implement, Deploy
4. **Lab 04** — Testing, Front-end, and AI Agents
5. **Lab 05** — Data Pipeline and Analytics Dashboard
6. **Lab 06** — Build Your Own Agent
7. **Lab 07** — Build a Client with an AI Coding Agent
8. **lab-08**

Just let me know which lab (e.g., "lab-04" or "Lab 04")!
## Task 3A — Structured logging

## Task 3A — Structured logging

### Happy-path log excerpt (request_started → request_completed, status 200)
```
2026-03-28 13:29:24,026 INFO [lms_backend.main] [main.py:62] [trace_id=96bf90919fd88435a21669f4475aed9a ...] - request_started
2026-03-28 13:29:24,026 INFO [lms_backend.auth] [auth.py:30] [trace_id=96bf90919fd88435a21669f4475aed9a ...] - auth_success
2026-03-28 13:29:24,026 INFO [lms_backend.db.items] [items.py:16] [trace_id=96bf90919fd88435a21669f4475aed9a ...] - db_query
2026-03-28 13:29:24,079 INFO [lms_backend.main] [main.py:74] [trace_id=96bf90919fd88435a21669f4475aed9a ...] - request_completed
INFO: 172.21.0.8:36626 - "GET /items/ HTTP/1.1" 200 OK
```

### Error-path log excerpt (db_query with error, postgres stopped)
```
socket.gaierror: [Errno -2] Name or service not known
2026-03-28 13:36:22,815 ERROR [lms_backend.db.items] [items.py:23] [trace_id=77d645637c76ba6ee54b133081ad89c4 ...] - db_query
2026-03-28 13:36:22,816 WARNING [lms_backend.routers.items] [items.py:23] [trace_id=77d645637c76ba6ee54b133081ad89c4 ...] - items_list_failed_as_not_found
2026-03-28 13:36:22,817 INFO [lms_backend.main] [main.py:74] [trace_id=77d645637c76ba6ee54b133081ad89c4 ...] - request_completed
INFO: 172.21.0.8:48490 - "GET /items/ HTTP/1.1" 404 Not Found
```

### VictoriaLogs query

Query used: `_time:1h service.name:"Learning Management Service" severity:ERROR`

Result: 8 error entries (unhandled_exception) from the period when PostgreSQL
was stopped. VictoriaLogs makes it easy to filter by service and severity
compared to grepping raw docker compose logs.

## Task 3B — Traces

### Healthy trace (trace_id: 96bf90919fd88435a21669f4475aed9a)

Span hierarchy:
- GET /items/ (root, 54ms, status 200)
  - connect (postgres connection, 39ms)
  - SELECT db-lab-8 (SQL query, 8ms)
  - BEGIN;
  - ROLLBACK;
  - GET /items/ http send (response, status 200)

### Error trace (trace_id: 77d645637c76ba6ee54b133081ad89c4)

Span hierarchy:
- GET /items/ (root, 276ms, status 404)
  - connect (postgres connection, 268ms, ERROR)
    - exception: socket.gaierror: [Errno -2] Name or service not known
    - otel.status_description: gaierror: Name or service not known
  - GET /items/ http send (response, status 404)

The error trace shows that when PostgreSQL is stopped, the connect span fails
with a DNS resolution error. The root span completes with status 404 instead
of 200, and no SQL query is executed since the connection itself failed.
## Task 3C — Observability MCP tools

## Task 3C — Observability MCP tools

### MCP tools registered

Four observability tools were implemented in `mcp/mcp-obs/src/mcp_obs/server.py`
and successfully registered with the agent:

- `mcp_obs_logs_search` — search logs using LogsQL query
- `mcp_obs_logs_error_count` — count errors per service over a time window
- `mcp_obs_traces_list` — list recent traces for a service
- `mcp_obs_traces_get` — fetch a specific trace by ID

Confirmed in nanobot logs: 

MCP server 'obs': connected, 4 tools registered
```

### Normal conditions response

Query: "Any LMS backend errors in the last 10 minutes?"

Agent was unable to respond due to Qwen API being blocked by Aliyun WAF
on the university VM network. The qwen-code-api logs show:
`RuntimeError: Token refresh returned a non-JSON response` —
the upstream Qwen authentication endpoint returns an HTML WAF page
instead of a JSON token response. This is a network-level infrastructure
issue, not a code issue.

### Failure conditions response

PostgreSQL was stopped and several LMS-backed requests were triggered.
The error trace (trace_id: 77d645637c76ba6ee54b133081ad89c4) confirmed
that the connect span failed with `socket.gaierror: Name or service not known`
and the root span completed with status 404.
## Task 4A — Multi-step investigation

<!-- Paste the agent's response to "What went wrong?" showing chained log + trace investigation -->

## Task 4B — Proactive health check

<!-- Screenshot or transcript of the proactive health report that appears in the Flutter chat -->

## Task 4C — Bug fix and recovery

<!-- 1. Root cause identified
     2. Code fix (diff or description)
     3. Post-fix response to "What went wrong?" showing the real underlying failure
     4. Healthy follow-up report or transcript after recovery -->
