from typing import List

from pydantic import BaseModel

from app.models.repository.fields import RepositoryFields


class RepositoryRequest(BaseModel):
    """Request model for repository parsing."""

    repository_url: str = RepositoryFields.repository_url


class RepositoryResponse(BaseModel):
    """Response model for repository parsing."""

    repository_url: str = RepositoryFields.repository_url
    parsed_repository: str = RepositoryFields.parsed_repository
    embedding_vector: List[float] = RepositoryFields.embedding_vector
