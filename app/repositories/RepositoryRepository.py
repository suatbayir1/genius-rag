from abc import ABC, abstractmethod
from typing import List


class RepositoryRepository(ABC):
    """Abstract repository class for a repository."""

    @abstractmethod
    def save(self, document: str, embedding: List[float], document_id: str) -> None:
        """Store the embedding vector in the database.

        Args:
            document (str): The document to store in the database.
            embedding (List[float]): The vector representation of the document.
            document_id (str): Unique identifier for the document.

        Returns:
            None
        """
