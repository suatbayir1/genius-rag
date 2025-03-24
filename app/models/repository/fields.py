from pydantic import Field, HttpUrl


class RepositoryFields:
    """Base model for repository-related fields."""

    repository_url: HttpUrl = Field(..., description="Repository URL")
