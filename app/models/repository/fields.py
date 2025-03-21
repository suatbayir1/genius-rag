from pydantic import Field


class RepositoryFields:
    """Base model for repository-related fields."""

    repository_url: str = Field(..., description="Repository URL")
