from typing import List

from sentence_transformers import SentenceTransformer

from app.config import settings
from app.services.abstract.embedding.embedding import Embedding


class SentenceTransformerEmbedding(Embedding):
    """Service for generating embeddings using the SentenceTransformer library."""

    def __init__(self):
        """Initialize the SentenceTransformer model."""
        self.model = SentenceTransformer(settings.EMBEDDING_MODEL_NAME)

    def encode(self, chunks: List[str]) -> List[float]:
        """Encode the input chunks into an embedding vector.

        Args:
            chunks (List[str]): The text to encode.

        Returns:
            List[float]: The embedding vector representation of the text.
        """
        return self.model.encode(chunks, batch_size=8, convert_to_numpy=True).tolist()
