from abc import ABC, abstractmethod

from pydantic import HttpUrl

from app.models.repository.models import RepositoryResponse


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
