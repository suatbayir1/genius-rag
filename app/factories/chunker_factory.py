from app.models.repository.enums import Language
from app.services.abstract.chunking.chunker import Chunker
from app.services.concrete.chunker.code_chunker import CodeChunker
from app.services.concrete.chunker.text_chunker import TextChunker


class ChunkerFactory:
    @staticmethod
    def get_chunker(language: str) -> Chunker:
        if Language.is_valid(language):
            return CodeChunker(language)
        return TextChunker()
