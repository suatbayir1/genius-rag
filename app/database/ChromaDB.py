from typing import Any, Dict, List

from chromadb import Collection, HttpClient

from app.config import settings


class ChromaDB:
    def __init__(self, host: str = settings.CHROMA_HOST, port: int = settings.CHROMA_PORT):
        """Instantiate ChromaDB HttpClient."""
        self.client = HttpClient(host=host, port=port)

    def _get_collection(self, collection_name: str) -> Collection:
        """Use specific collection of ChromaDB.

        Args:
            collection_name (str): Collection name

        Returns:
            Collection: Collection of ChromaDB
        """
        return self.client.get_or_create_collection(collection_name)

    def save(
        self,
        collection_name: str,
        ids: List[str],
        documents: List[str],
        embeddings: List[List[float]],
        metadatas: List[Dict[str, Any]],
    ) -> None:
        """Save documents to collection in ChromaDB.

        Args:
            collection_name (str): Collection name
            ids (List[str]): Ids of documents
            documents (List[str]): Chunks as document
            embeddings (List[List[float]]): Numerical values as embeddings
            metadatas (List[Dict[str, Any]]): List of dict as metadatas
        """
        collection = self._get_collection(collection_name)
        collection.add(ids=ids, documents=documents, embeddings=embeddings, metadatas=metadatas)

    def query(
        self,
        collection_name: str,
        query_embeddings: List[List[float]],
        top_k: int,
    ) -> Dict[str, Any]:
        """Find similar document using embeddings.

        Args:
            collection_name (str): Collection name
            query_embeddings (List[List[float]]): Embeddings of query
            top_k (int): Similar top k result

        Returns:
            Dict[str, Any]: Similar documents
        """
        collection = self._get_collection(collection_name)
        results = collection.query(query_embeddings=query_embeddings, n_results=top_k)
        return results

    def delete(
        self,
        collection_name: str,
        ids: List[str],
    ) -> None:
        """Delete documents using ids from collection.

        Args:
            collection_name (str): Collection name
            ids (List[str]): List of ids of documents
        """
        collection = self._get_collection(collection_name)
        collection.delete(ids=ids)

    def get_existing_ids(self, collection_name: str) -> set:
        """Return existing ids in collection.

        Args:
            collection_name (str): Collection name

        Returns:
            set: List of ids exists in collection
        """
        collection = self._get_collection(collection_name)
        existing_items = collection.get(include=[])
        return set(existing_items["ids"])
