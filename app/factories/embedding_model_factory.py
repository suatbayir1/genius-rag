from app.models.repository.enums import Language
from app.services.abstract.embedding.embedding import Embedding
from app.services.concrete.embedding.code_embedding import CodeEmbedding
from app.services.concrete.embedding.sentence_transformer_embedding import (
    SentenceTransformerEmbedding,
)


class EmbeddingModelFactory:
    @staticmethod
    def get_embedding_model(language: str) -> Embedding:
        if Language.is_valid(language):
            return CodeEmbedding()
        return SentenceTransformerEmbedding()
