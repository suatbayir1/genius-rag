from app.services.abstract.embedding.embedding import Embedding
from app.services.concrete.embedding.sentence_transformer_embedding import (
    SentenceTransformerEmbedding,
)


def get_embedding_service() -> Embedding:
    """Return an instance of SentenceTransformerEmbedding, implementing the Embedding interface."""
    return SentenceTransformerEmbedding()
