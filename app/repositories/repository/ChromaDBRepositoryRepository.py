import uuid
from typing import Any, Dict, List

import chromadb

from app.config import settings
from app.repositories.RepositoryRepository import RepositoryRepository


class ChromaDBRepositoryRepository(RepositoryRepository):
    """Implement the ChromaDB repository using Repository interface."""

    def __init__(self):
        """Initialize the ChromaDB client and collection."""
        self.client = chromadb.PersistentClient(path=settings.VECTOR_DB_PATH)

    def _get_collection(self, collection_name: str) -> chromadb.Collection:
        return self.client.get_or_create_collection(collection_name)

    def save(
        self, collection_name: str, ids: List[uuid.UUID], embeddings: List[float], metadatas: List[dict[str, Any]]
    ) -> None:
        """Save the document and its embedding vector to the collection.

        Args:
            ids (List[uuid.UUID]): Unique identifiers for the document.
            embeddings (List[float]): The vector representation of the document.
            metadatas (List[dict[str, Any]]): The metadatas to store in the database.
        """
        collection = self._get_collection(collection_name)
        collection.add(ids=ids, embeddings=embeddings, metadatas=metadatas)

    def query(self, collection_name: str, query_embeddings: List[float], top_k: int) -> Dict[str, Any]:
        """Query the vector database.

        Args:
            collection_name (str): The name of the collection to query.
            query_embeddings (List[float]): The vector representation of the query.
            top_k (int): The number of top results to return."
        """
        collection = self._get_collection(collection_name)
        results = collection.query(query_embeddings=query_embeddings, n_results=top_k)
        return results
