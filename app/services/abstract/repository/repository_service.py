from abc import ABC, abstractmethod

from app.models.repository.models import RepositoryResponse


class RepositoryService(ABC):
    """Abstract base class for a repository service."""

    @abstractmethod
    def process(self, repository_url: str) -> RepositoryResponse:
        """Process a repository.

        Args:
            repository_url (str): The URL of the repository to process.

        Returns:
            str: The processed repository.
        """
