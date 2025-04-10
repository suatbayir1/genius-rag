from app.factories.constants import DOCLING_SUPPORTED_DOCUMENTS
from app.models.repository.enums import Language
from app.services.abstract.chunking.chunker import Chunker
from app.services.concrete.chunker.code_chunker import CodeChunker
from app.services.concrete.chunker.docling_chunker import DoclingChunker
from app.services.concrete.chunker.text_chunker import TextChunker


class ChunkerFactory:
    @staticmethod
    def get_chunker(extension: str) -> Chunker:
        if Language.is_valid(extension):
            return CodeChunker(extension)

        if extension in DOCLING_SUPPORTED_DOCUMENTS:
            return DoclingChunker()

        return TextChunker()
