from app.models.repository.enums import Language
from app.services.abstract.embedding.embedding import Embedding
from app.services.concrete.embedding.code_embedding import CodeEmbedding
from app.services.concrete.embedding.text_embedding import TextEmbedding


class EmbeddingModelFactory:
    @staticmethod
    def get_embedding_model(language: str) -> Embedding:
        if Language.is_valid(language):
            return CodeEmbedding()
        return TextEmbedding()

    @staticmethod
    def get_embedding(cls: type[Embedding]) -> Embedding:
        return cls()
