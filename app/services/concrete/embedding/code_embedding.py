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

    def encode(self, chunks: List[str]) -> List[List[float]]:
        inputs = self.tokenizer(chunks, return_tensors="pt", truncation=True, max_length=512, padding="max_length").to(
            self.DEVICE
        )

        with torch.no_grad():
            outputs = self.model(**inputs)

        return outputs.cpu().numpy().tolist()
