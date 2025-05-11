from typing import List

from langchain_ollama import OllamaEmbeddings

from app.config import settings
from app.services.abstract.embedding.embedding import Embedding


class OllamaEmbedding(Embedding):
    DEVICE: str = "cuda" if settings.USE_GPU else "cpu"

    def __init__(self, model_name: str = "nomic-embed-text"):
        """Initialize the OllamaEmbedding model."""
        self.model: OllamaEmbeddings = OllamaEmbeddings(model=model_name, base_url=settings.OLLAMA_BASE_URL)

    def encode(self, chunks: List[str]) -> List[List[float]]:
        return self.model.embed_documents(chunks)
