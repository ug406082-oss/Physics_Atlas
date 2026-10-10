#!/usr/bin/env bash
# One-time setup: build the sandbox image and pull the local model.
# This is the ONLY step that uses the network; the running sandbox does not.
set -euo pipefail
cd "$(dirname "$0")"

MODEL="${OLLAMA_MODEL:-qwen2.5-coder:7b}"
VOLUME="physics-atlas-ollama-models"

echo "[1/2] Building the opencode image..."
docker compose build

echo "[2/2] Pulling '${MODEL}' into the sandbox model volume (one-time, network required)..."
docker volume create "$VOLUME" >/dev/null
docker run --rm --network host \
  -v "${VOLUME}":/root/.ollama \
  ollama/ollama:latest pull "${MODEL}"

echo
echo "Done. Start the sandbox with:"
echo "    docker compose up -d model"
echo "    docker compose run --rm opencode"
