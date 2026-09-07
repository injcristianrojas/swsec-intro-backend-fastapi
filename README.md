# swsec-intro-backend-fastapi

Run using `uv run fastapi dev --port 9000`

## Dockerized version

```shell
make docker_build
make docker_run
```

# Agentic dev mode (using Claude Code + Zed + Podman)

Go to the claude directory and run

```shell
podman build -t claude-code-acp:latest .
```

Then add to Zed's config.json's `agent-servers` section:

```json
"Claude (Podman sandbox)": {
  "type": "custom",
  "command": "<claude-container-runner.sh location>",
  "args": [],
  "env": {}
},
```
