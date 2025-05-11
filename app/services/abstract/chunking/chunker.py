from abc import ABC, abstractmethod
from typing import List

from langchain.schema.document import Document


class Chunker(ABC):
    """Abstract base class for a chunker."""

    @abstractmethod
    def chunk(self, file_path: str) -> List[str]:
        """Chunk text into smaller parts.

        Args:
            file_path (str): The path of the file to chunk.

        Returns:
            List[str]: The chunked text.
        """

    def calculate_chunk_ids(self, chunks: list[Document]) -> list[Document]:
        """Create IDs like Page Source : Page Number : Chunk Index.

        Args:
            chunks (list[Document])): Chunks of the document.

        Returns:
            List[str]: The chunked text.
        """
        last_page_id = None
        current_chunk_index = 0

        for chunk in chunks:
            source = chunk.metadata.get("source")
            page = chunk.metadata.get("page")
            current_page_id = f"{source}:{page}"

            # If the page ID is the same as the last one, increment the index.
            if current_page_id == last_page_id:
                current_chunk_index += 1
            else:
                current_chunk_index = 0

            # Calculate the chunk ID.
            chunk_id = f"{current_page_id}:{current_chunk_index}"
            last_page_id = current_page_id

            # Add it to the page meta-data.
            chunk.metadata["id"] = chunk_id

        return chunks
