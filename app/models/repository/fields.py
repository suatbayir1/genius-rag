from typing import List

from pydantic import Field


class RepositoryFields:
    """Base model for repository-related fields."""

    repository_url: str = Field(..., description="Repository URL")
    parsed_repository: str = Field(..., description="Parsed repository")
    embedding_vector: List[float] = Field(..., description="Embedding vector")
