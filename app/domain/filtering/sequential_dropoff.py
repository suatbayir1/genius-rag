from typing import Any, Dict, List, Tuple

from app.domain.filtering.document_filter import DocumentFilter


class SequentialDropOffFilter(DocumentFilter):
    def filter(
        self,
        documents: List[str],
        metadatas: List[Dict[str, Any]],
        distances: List[float],
    ) -> Tuple[List[str], List[Dict[str, Any]], List[int]]:
        if not documents:
            return [], [], []

        filtered_docs = []
        filtered_meta = []
        filtered_scores: List[int] = []

        for i in range(0, len(distances)):
            similarity = 1 - distances[i]
            percentage = int(similarity * 100)

            # Do not use this chunk if the cosine distance is greater than 0.80
            if percentage < 20:
                break

            if i == 0:
                filtered_docs.append(documents[i])
                filtered_meta.append(metadatas[i])
                filtered_scores.append(percentage)
                continue

            diff = distances[i] - distances[i - 1]

            # Do not use subsequent chunks if the distance between chunks increases abruptly
            if diff > distances[0]:
                break

            filtered_docs.append(documents[i])
            filtered_meta.append(metadatas[i])
            filtered_scores.append(percentage)

        return filtered_docs, filtered_meta, filtered_scores
