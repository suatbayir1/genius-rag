#!/bin/bash

OLLAMA_CONTAINER_NAME="ollama"

# check model is exists ?
MODEL_EXISTS=$(docker exec $OLLAMA_CONTAINER_NAME ollama list models | grep "llama3.2")

if [ -z "$MODEL_EXISTS" ]; then
  echo "Model downlading..."
  docker exec $OLLAMA_CONTAINER_NAME ollama pull llama3.2
else
  echo "Model exists..."
fi
