from app.services.abstract.chunking.chunker import Chunker


class TextChunker(Chunker):
    def chunk(self, file_path: str) -> list[str]:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                return f.read().split("\n")
        except UnicodeDecodeError:
            return []
