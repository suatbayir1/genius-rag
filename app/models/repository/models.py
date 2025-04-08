from typing import Any, Dict, List

from pydantic import BaseModel, HttpUrl

from app.models.repository.fields import QueryFields, RepositoryFields


class RepositoryRequest(BaseModel):
    """Request model for repository parsing."""

    repository_url: HttpUrl = RepositoryFields.repository_url


class RepositoryResponse(BaseModel):
    """Response model for repository parsing."""

    repository_url: HttpUrl = RepositoryFields.repository_url


class QueryRequest(BaseModel):
    """Request model for repository querying."""

    query: str = QueryFields.query
    top_k: int = QueryFields.top_k


class QueryResponse(BaseModel):
    """Response model for repository querying."""

    documents: Dict[str, Any] = QueryFields.documents


class QueryResult(BaseModel):
    """Model for individual query results."""

    id: str = QueryFields.id
    embedding: List[float] = QueryFields.embedding
    metadata: Dict[str, Any] = QueryFields.metadata
