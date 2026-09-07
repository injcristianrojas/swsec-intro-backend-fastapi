#!/bin/bash

exec podman run -i --rm \
  --userns=keep-id \
  -v "$HOME/.claude:$HOME/.claude:Z" \
  -v "$PWD:/workspace" \
  -w /workspace \
  -e CLAUDE_CONFIG_DIR="$HOME/.claude" \
  claude-code-acp-sandbox \
  npx @agentclientprotocol/claude-agent-acp@latest --acp
