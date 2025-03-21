from app.services.abstract.embedding.embedding_service import EmbeddingService
from app.services.concrete.embedding.sentence_transformer_service import (
    SentenceTransformerService,
)


def get_embedding_service() -> EmbeddingService:
    """Return an instance of SentenceTransformerService, implementing the EmbeddingService interface."""
    return SentenceTransformerService()
