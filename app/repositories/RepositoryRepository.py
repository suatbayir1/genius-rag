from abc import ABC, abstractmethod
from typing import Any, Dict, List


class RepositoryRepository(ABC):
    """Abstract repository class for a repository."""

    @abstractmethod
    def save(
        self,
        collection_name: str,
        ids: List[str],
        chunks: List[str],
        embeddings: List[float],
        metadatas: List[dict[str, Any]],
    ) -> None:
        """Store the embeddings vector in the database.

        Args:
            collection_name (str): The name of the collection to store the embeddings.
            ids (List[str]): Unique identifiers for the document.
            chunks: List[str]: The text chunks to store in the database.
            embeddings (List[float]): The vector representation of the document.
            metadatas (List[dict[str, Any]]): The metadatas to store in the database.

        Returns:
            None
        """

    @abstractmethod
    def query(self, collection_name: str, query_embeddings: List[float], top_k: int) -> Dict[str, Any]:
        """Query the vector database.

        Args:
            collection_name (str): The name of the collection to query.
            query_embeddings (List[float]): The vector representation of the query.
            top_k (int): The number of top results to return.

        Returns:
            List[dict[str, Any]]: The most relevant stored documents.
        """
