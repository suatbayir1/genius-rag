#!/bin/bash

set -e

echo "Starting Ollama Server..."
ollama serve &

sleep 5

echo "Pulling model llama3.2..."
ollama pull llama3.2

wait
