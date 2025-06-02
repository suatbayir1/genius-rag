from abc import ABC, abstractmethod
from typing import Any, Dict, List, Tuple


class DocumentFilter(ABC):
    """Filter documents."""

    @abstractmethod
    def filter(
        self,
        documents: List[str],
        metadatas: List[Dict[str, Any]],
        distances: List[float],
    ) -> Tuple[List[str], List[Dict[str, Any]], List[int]]:
        pass
