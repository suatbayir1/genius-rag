import os
from typing import List

import torch
from transformers import AutoModel, AutoTokenizer

from app.config import settings
from app.services.abstract.embedding.embedding import Embedding


class CodeEmbedding(Embedding):
    DEVICE: str = "cuda" if settings.USE_GPU else "cpu"

    def __init__(self):
        """Initialize the CodeEmbedding model."""
        model_path = os.path.join(settings.HF_MODEL_DIRECTORY, settings.CODE_EMBEDDING_MODEL)
        self.tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True, local_files_only=True)
        self.model = AutoModel.from_pretrained(model_path, trust_remote_code=True, local_files_only=True).to(
            self.DEVICE
        )

    def encode(self, chunks: List[str]) -> List[List[float]]:
        inputs = self.tokenizer(chunks, return_tensors="pt", truncation=True, max_length=512, padding="max_length").to(
            self.DEVICE
        )

        with torch.no_grad():
            outputs = self.model(**inputs)

        return outputs.cpu().numpy().tolist()
