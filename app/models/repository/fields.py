from typing import Any, Dict, List

from pydantic import Field, HttpUrl


class RepositoryFields:
    """Base model for repository-related fields."""

    repository_url: HttpUrl = Field(..., description="Repository URL")


class QueryFields:
    """Base model for query-related fields."""

    query: str = Field(..., description="Query string")
    top_k: int = Field(3, description="Number of top results to return")
    documents: Dict[str, Any] = Field(..., description="List of the most relevant stored documents.")
    id: str = Field(..., description="Unique identifier for the document.")
    embedding: List[float] = Field(..., description="Vector representation of the document.")
    metadata: Dict[str, Any] = Field(..., description="Metadata associated with the document.")
