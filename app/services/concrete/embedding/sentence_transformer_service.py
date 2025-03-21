from typing import List

from sentence_transformers import SentenceTransformer

from app.config import settings
from app.services.abstract.embedding.embedding_service import EmbeddingService


class SentenceTransformerService(EmbeddingService):
    """Service for generating embeddings using the SentenceTransformer library."""

    def __init__(self):
        """Initialize the SentenceTransformer model."""
        self.embedding_model = SentenceTransformer(settings.EMBEDDING_MODEL_NAME)

    def encode(self, text: str) -> List[float]:
        """Encode the input text into an embedding vector.

        Args:
            text (str): The text to encode.

        Returns:
            List[float]: The embedding vector representation of the text.
        """
        return self.embedding_model.encode(text).tolist()
