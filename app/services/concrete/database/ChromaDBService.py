from typing import List

import chromadb

from app.config import settings
from app.services.abstract.database.VectorDBService import VectorDBService


class ChromaDBService(VectorDBService):
    """Implement the VectorDBService interface using ChromaDB."""

    def __init__(self):
        """Initialize the ChromaDB client and collection."""
        self.client = chromadb.PersistentClient(path=settings.VECTOR_DB_PATH)
        self.collection = self.client.get_or_create_collection("repositories")

    def save(self, document: str, embedding: List[float], document_id: str) -> None:
        """Save the document and its embedding vector to the collection.

        Args:
            document (str): The document to store in the database.
            embedding (List[float]): The vector representation of the document.
            document_id (str): Unique identifier for the document.
        """
        self.collection.add(documents=[document], embeddings=[embedding], ids=[document_id])
