from typing import Any, Dict, List, Tuple

from app.domain.filtering.document_filter import DocumentFilter


class SequentialDropOffFilter(DocumentFilter):
    def filter(
        self,
        documents: List[str],
        metadatas: List[Dict[str, Any]],
        distances: List[float],
    ) -> Tuple[List[str], List[Dict[str, Any]]]:
        if not documents:
            return [], []

        filtered_docs = [documents[0]]
        filtered_meta = [metadatas[0]]

        for i in range(1, len(distances)):
            diff = distances[i] - distances[i - 1]

            if diff > distances[0]:
                break

            filtered_docs.append(documents[i])
            filtered_meta.append(metadatas[i])

        return filtered_docs, filtered_meta
