from typing import List

import tree_sitter_python
from tree_sitter import Language, Parser

from app.services.abstract.chunking.chunker import Chunker


class CodeChunker(Chunker):
    """Code Chunker for chunking code into smaller parts."""

    LANGUAGES = {
        "python": Language(tree_sitter_python.language()),
    }

    def __init__(self, language: str):
        """Initialize the CodeChunker service."""
        self.parser = Parser(self.LANGUAGES[language])

    def chunk(self, text: str) -> List[str]:
        """Chunk code into smaller parts.

        Args:
            text (str): The code to chunk.

        Returns:
            List[str]: The chunked code.
        """
        tree = self.parser.parse(text.encode())
        root_node = tree.root_node

        chunks = []
        for child in root_node.children:
            chunk = text[child.start_byte : child.end_byte]
            chunks.append(chunk)
        return chunks if chunks else [text]
