from typing import Any, Dict, List

from app.database.ChromaDB import ChromaDB
from app.repositories.document_repository import DocumentRepository


class ChromaDBDocumentRepository(DocumentRepository):
    """Implement the ChromaDB repository using DocumentRepository interface."""

    def __init__(self):
        """Initialize the ChromaDB client and collection."""
        self.db = ChromaDB()

    def get_existing_ids(self, collection_name: str) -> set:
        return self.db.get_existing_ids(collection_name)

    def save(
        self,
        collection_name: str,
        ids: List[str],
        chunks: List[str],
        embeddings: List[List[float]],
        metadatas: List[dict[str, Any]],
    ) -> None:
        """Save the document and its embedding vector to the collection.

        Args:
            ids (List[str]): Unique identifiers for the document.
            chunks (List): List of chunks
            embeddings (List[float]): The vector representation of the document.
            metadatas (List[dict[str, Any]]): The metadatas to store in the database.
        """
        self.db.save(collection_name, ids, chunks, embeddings, metadatas)

    def query(self, collection_name: str, query_embeddings: List[List[float]], top_k: int) -> Dict[str, Any]:
        """Query the vector database.

        Args:
            collection_name (str): The name of the collection to query.
            query_embeddings (List[float]): The vector representation of the query.
            top_k (int): The number of top results to return."
        """
        return self.db.query(collection_name, query_embeddings, top_k)
