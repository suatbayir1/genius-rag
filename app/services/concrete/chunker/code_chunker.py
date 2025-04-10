import os
from typing import List, Optional

import tree_sitter_python
from tree_sitter import Language, Parser, Tree

from app.services.abstract.chunking.chunker import Chunker


class CodeChunker(Chunker):
    """Code Chunker for chunking code into smaller parts."""

    LANGUAGES = {
        ".py": Language(tree_sitter_python.language()),
    }

    def __init__(self, language: str):
        """Initialize the CodeChunker service."""
        self.parser = Parser(self.LANGUAGES[language])

    def chunk(self, file_path: str) -> List[str]:
        """Chunk code into smaller parts.

        Args:
            file_path (str): The path of the file to chunk.

        Returns:
            List[str]: The chunked code.
        """
        text: Optional[str] = self._read_file(file_path)
        if not text:
            return []

        tree = self.parser.parse(text.encode())

        return self._extract_chunks(text, tree)

    def _read_file(self, file_path: str) -> Optional[str]:
        if not os.path.exists(file_path):
            return None

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                return f.read()
        except UnicodeDecodeError:
            return None

    def _extract_chunks(self, text: str, tree: Tree) -> List[str]:
        root_node = tree.root_node

        chunks = [
            text[child.start_byte : child.end_byte] for child in root_node.children if child.end_byte > child.start_byte
        ]

        return chunks or [text]
