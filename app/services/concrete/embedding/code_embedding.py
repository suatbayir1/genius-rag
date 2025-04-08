from typing import List

import torch
from transformers import AutoModel, AutoTokenizer

from app.config import settings
from app.services.abstract.embedding.embedding import Embedding


class CodeEmbedding(Embedding):
    CODE_EMBEDDING_MODEL: str = "Salesforce/codet5p-110m-embedding"
    DEVICE: str = "cuda" if settings.USE_GPU else "cpu"

    def __init__(self):
        """Initialize the CodeEmbedding model."""
        self.tokenizer = AutoTokenizer.from_pretrained(self.CODE_EMBEDDING_MODEL, trust_remote_code=True)
        self.model = AutoModel.from_pretrained(self.CODE_EMBEDDING_MODEL, trust_remote_code=True).to(self.DEVICE)

    def encode(self, chunks: List[str]) -> List[float]:
        embeddings: List[float] = []
        for chunk in chunks:
            inputs = self.tokenizer.encode(chunk, return_tensors="pt").to(self.DEVICE)

            with torch.no_grad():
                embedding = self.model(inputs)[0]
            embeddings.append(embedding.cpu().numpy().tolist())

        return embeddings
