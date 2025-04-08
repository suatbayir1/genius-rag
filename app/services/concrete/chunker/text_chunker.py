from app.services.abstract.chunking.chunker import Chunker


class TextChunker(Chunker):
    def chunk(self, text: str) -> list[str]:
        """Split the text into chunks of specified size."""
        return text.split("\n\n")
