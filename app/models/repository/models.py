from pydantic import BaseModel, HttpUrl

from app.models.repository.fields import RepositoryFields


class RepositoryRequest(BaseModel):
    """Request model for repository parsing."""

    repository_url: HttpUrl = RepositoryFields.repository_url


class RepositoryResponse(BaseModel):
    """Response model for repository parsing."""

    repository_url: HttpUrl = RepositoryFields.repository_url
