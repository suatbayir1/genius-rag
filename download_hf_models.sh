#!/bin/bash

# List of model IDs (add as many as you need)
MODEL_IDS=(
  "Salesforce/codet5p-110m-embedding"
  "ds4sd/SmolDocling-256M-preview"
  "sentence-transformers/all-MiniLM-L6-v2"
  "HuggingFaceTB/SmolVLM-256M-Instruct"
  "unitary/toxic-bert"
)

# Base directory
BASE_DIR="/opt/hf_models"

# Make sure base directory exists
mkdir -p "$BASE_DIR"

# Loop through each model and download
for MODEL_ID in "${MODEL_IDS[@]}"; do
  TARGET_DIR="$BASE_DIR/$MODEL_ID"

  echo "📦 Downloading: $MODEL_ID → $TARGET_DIR"

python - <<EOF
from huggingface_hub import snapshot_download

snapshot_download(
    repo_id="$MODEL_ID",
    local_dir="$TARGET_DIR",
    local_dir_use_symlinks=False
)
EOF

  echo "✅ Downloaded: $MODEL_ID"
done

echo "🎉 All models downloaded to: $BASE_DIR"
