from typing import Any, Dict, List, Tuple

from app.domain.filtering.document_filter import DocumentFilter


class SequentialDropOffFilter(DocumentFilter):
    def __init__(self, similarity_threshold: int) -> None:
        """Set similarity threshold."""
        self.similarity_threshold = similarity_threshold

    def filter(
        self,
        documents: List[str],
        metadatas: List[Dict[str, Any]],
        distances: List[float],
    ) -> Tuple[List[str], List[Dict[str, Any]], List[int]]:
        """Filter similar records by distances between records.

        Args:
            documents (List[str]): Documents
            metadatas (List[Dict[str, Any]]): Metadatas
            distances (List[float]): Distances

        Returns:
            Tuple[List[str], List[Dict[str, Any]], List[int]]: similar documents, metadatas and distances
        """
        if not documents:
            return [], [], []

        max_distance: float = 0.0
        max_distance_index: int = 0

        for i in range(1, len(distances)):
            distance = distances[i] - distances[i - 1]

            if distance >= max_distance:
                max_distance = distance
                max_distance_index = i

        docs = documents[: max_distance_index + 1]
        metas = metadatas[: max_distance_index + 1]
        dists = distances[: max_distance_index + 1]

        filtered_docs: List[str] = []
        filtered_meta: List[Dict[str, Any]] = []
        filtered_scores: List[int] = []

        for i in range(len(dists)):
            similarity = 1 - dists[i]
            percentage = int(similarity * 100)

            # Do not use this chunk if the cosine distance is greater than 0.50
            if percentage >= self.similarity_threshold:
                filtered_docs.append(docs[i])
                filtered_meta.append(metas[i])
                filtered_scores.append(percentage)

        return filtered_docs, filtered_meta, filtered_scores
