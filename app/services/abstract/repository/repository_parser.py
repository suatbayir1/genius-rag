from abc import ABC, abstractmethod


class RepositoryParser(ABC):
    """Abstract base class for a repository parser."""

    @abstractmethod
    def parse(self, repository_url: str) -> str:
        """Parse the contents of a repository.

        Args:
            repository_url (str): The URL of the repository to parse.

        Returns:
            str: The parsed contents of the repository.
        """
