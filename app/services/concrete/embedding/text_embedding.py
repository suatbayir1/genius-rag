from typing import List

import torch
from transformers import AutoModel, AutoTokenizer

from app.config import settings
from app.services.abstract.embedding.embedding import Embedding


class TextEmbedding(Embedding):
    MODEL: str = "ds4sd/SmolDocling-256M-preview"
    DEVICE: str = "cuda" if settings.USE_GPU else "cpu"

    def __init__(self):
        """Initialize the CodeEmbedding model."""
        self.tokenizer = AutoTokenizer.from_pretrained(self.MODEL)
        self.model = AutoModel.from_pretrained(self.MODEL)

    def encode(self, chunks: List[str]) -> List[float]:
        inputs = self.tokenizer(chunks, padding=True, truncation=True, return_tensors="pt")

        with torch.no_grad():
            outputs = self.model(**inputs)
            embeddings = outputs.last_hidden_state.mean(dim=1)

        return embeddings.tolist()
