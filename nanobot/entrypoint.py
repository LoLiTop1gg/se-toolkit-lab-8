import json
import os

config_path = "/app/nanobot/config.json"
workspace_path = "/app/nanobot/workspace"

with open(config_path) as f:
    config = json.load(f)

# LLM provider
config["providers"]["custom"]["apiKey"] = os.environ.get("LLM_API_KEY", "")
config["providers"]["custom"]["apiBase"] = os.environ.get("LLM_API_BASE_URL", "")
config["agents"]["defaults"]["model"] = os.environ.get("LLM_API_MODEL", "coder-model")

# Gateway
config["gateway"]["host"] = os.environ.get("NANOBOT_GATEWAY_CONTAINER_ADDRESS", "0.0.0.0")
config["gateway"]["port"] = int(os.environ.get("NANOBOT_GATEWAY_CONTAINER_PORT", "18790"))

# MCP LMS
config["tools"]["mcpServers"]["lms"]["env"] = {
    "NANOBOT_LMS_BACKEND_URL": os.environ.get("NANOBOT_LMS_BACKEND_URL", ""),
    "NANOBOT_LMS_API_KEY": os.environ.get("NANOBOT_LMS_API_KEY", ""),
}

# MCP webchat
webchat_address = os.environ.get("NANOBOT_WEBCHAT_CONTAINER_ADDRESS", "0.0.0.0")
webchat_port = int(os.environ.get("NANOBOT_WEBCHAT_CONTAINER_PORT", "18791"))
access_key = os.environ.get("NANOBOT_ACCESS_KEY", "")

config["tools"]["mcpServers"]["webchat"] = {
    "command": "python",
    "args": ["-m", "mcp_webchat"],
    "env": {
        "WEBCHAT_UI_RELAY_URL": f"http://{webchat_address}:{webchat_port}",
        "WEBCHAT_ACCESS_TOKEN": access_key,
    }
}

# Webchat channel
config["channels"]["webchat"] = {
    "enabled": True,
    "host": webchat_address,
    "port": webchat_port,
    "accessKey": access_key,
    "allowFrom": ["*"]
}

resolved_path = "/app/nanobot/config.resolved.json"
with open(resolved_path, "w") as f:
    json.dump(config, f, indent=2)

print(f"Using config: {resolved_path}")

os.execvp("nanobot", ["nanobot", "gateway", "--config", resolved_path, "--workspace", workspace_path])
