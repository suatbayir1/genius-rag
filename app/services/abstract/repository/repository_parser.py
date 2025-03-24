from abc import ABC, abstractmethod

from pydantic import HttpUrl


class RepositoryParser(ABC):
    """Abstract base class for a repository parser."""

    @abstractmethod
    def parse(self, repository_url: HttpUrl) -> str:
        """Parse the contents of a repository.

        Args:
            repository_url (HttpUrl): The URL of the repository to parse.

        Returns:
            str: The parsed contents of the repository.
        """
