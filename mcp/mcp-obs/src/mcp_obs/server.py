import os
import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("obs")

VICTORIA_LOGS_URL = os.environ.get("VICTORIA_LOGS_URL", "http://victorialogs:9428")
VICTORIA_TRACES_URL = os.environ.get("VICTORIA_TRACES_URL", "http://victoriatraces:10428")


@mcp.tool()
def logs_search(query: str, limit: int = 20) -> str:
    """Search logs using LogsQL query. Example query: _time:10m service.name:"Learning Management Service" severity:ERROR"""
    try:
        resp = httpx.get(
            f"{VICTORIA_LOGS_URL}/select/logsql/query",
            params={"query": query, "limit": limit},
            timeout=10,
        )
        resp.raise_for_status()
        lines = resp.text.strip().split("\n")
        return "\n".join(lines[:limit]) if lines else "No logs found"
    except Exception as e:
        return f"Error querying logs: {e}"


@mcp.tool()
def logs_error_count(service: str, time_window: str = "10m") -> str:
    """Count errors per service over a time window. service example: 'Learning Management Service'"""
    try:
        query = f'_time:{time_window} service.name:"{service}" severity:ERROR'
        resp = httpx.get(
            f"{VICTORIA_LOGS_URL}/select/logsql/query",
            params={"query": query, "limit": 1000},
            timeout=10,
        )
        resp.raise_for_status()
        lines = [l for l in resp.text.strip().split("\n") if l]
        return f"Found {len(lines)} errors for '{service}' in last {time_window}"
    except Exception as e:
        return f"Error counting logs: {e}"


@mcp.tool()
def traces_list(service: str, limit: int = 10) -> str:
    """List recent traces for a service. service example: 'Learning Management Service'"""
    try:
        resp = httpx.get(
            f"{VICTORIA_TRACES_URL}/select/jaeger/api/traces",
            params={"service": service, "limit": limit},
            timeout=10,
        )
        resp.raise_for_status()
        data = resp.json()
        traces = data.get("data", [])
        if not traces:
            return "No traces found"
        result = []
        for t in traces:
            tid = t.get("traceID", "")
            spans = t.get("spans", [])
            root = next((s for s in spans if not s.get("references")), spans[0] if spans else {})
            op = root.get("operationName", "")
            duration = root.get("duration", 0)
            tags = {tag["key"]: tag["value"] for tag in root.get("tags", [])}
            status = tags.get("http.status_code", "?")
            result.append(f"traceID={tid} op={op} duration={duration}us status={status}")
        return "\n".join(result)
    except Exception as e:
        return f"Error listing traces: {e}"


@mcp.tool()
def traces_get(trace_id: str) -> str:
    """Fetch a specific trace by ID and return span summary."""
    try:
        resp = httpx.get(
            f"{VICTORIA_TRACES_URL}/select/jaeger/api/traces/{trace_id}",
            timeout=10,
        )
        resp.raise_for_status()
        data = resp.json()
        traces = data.get("data", [])
        if not traces:
            return "Trace not found"
        spans = traces[0].get("spans", [])
        result = []
        for s in spans:
            op = s.get("operationName", "")
            duration = s.get("duration", 0)
            tags = {tag["key"]: tag["value"] for tag in s.get("tags", [])}
            error = tags.get("error", "false")
            status = tags.get("http.status_code", "")
            line = f"span={op} duration={duration}us"
            if status:
                line += f" status={status}"
            if error == "true":
                line += " ERROR"
            result.append(line)
        return "\n".join(result)
    except Exception as e:
        return f"Error fetching trace: {e}"


if __name__ == "__main__":
    mcp.run()
