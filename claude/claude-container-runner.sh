#!/usr/bin/env bash

exec podman run --rm -i \
  --userns=keep-id \
  -e HOME="$HOME" \
  -v "$HOME/workspace:$HOME/workspace:Z" \
  -v "$HOME/.claude:$HOME/.claude:Z" \
  -w "$HOME/workspace" \
  claude-code-acp:latest
