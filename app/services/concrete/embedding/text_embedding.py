import os
from typing import List

import torch
from transformers import AutoModel, AutoTokenizer

from app.config import settings
from app.services.abstract.embedding.embedding import Embedding


class TextEmbedding(Embedding):
    DEVICE: str = "cuda" if settings.USE_GPU else "cpu"

    def __init__(self):
        """Initialize the CodeEmbedding model."""
        model_path: str = os.path.join(settings.HF_MODEL_DIRECTORY, settings.TEXT_EMBEDDING_MODEL)
        self.tokenizer = AutoTokenizer.from_pretrained(model_path, local_files_only=True)
        self.model = AutoModel.from_pretrained(model_path, local_files_only=True)

    def encode(self, chunks: List[str]) -> List[List[float]]:
        inputs = self.tokenizer(chunks, padding=True, truncation=True, return_tensors="pt")

        with torch.no_grad():
            outputs = self.model(**inputs)
            embeddings = outputs.last_hidden_state.mean(dim=1)

        return embeddings.cpu().numpy().tolist()
