from abc import ABC, abstractmethod

from pydantic import HttpUrl

from app.models.repository.models import QueryRequest, QueryResponse, RepositoryResponse


class RepositoryService(ABC):
    """Abstract base class for a repository service."""

    @abstractmethod
    def process(self, repository_url: HttpUrl) -> RepositoryResponse:
        """Process a repository.

        Args:
            repository_url (HttpUrl): The URL of the repository to process.

        Returns:
            RepositoryResponse: The processed repository.
        """

    @abstractmethod
    def query(self, request: QueryRequest) -> QueryResponse:
        """Query the repository.

        Args:
            request (QueryRequest): The query request.

        Returns:
            QueryResponse: The query response.
        """
