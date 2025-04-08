from abc import ABC, abstractmethod
from typing import Generator


class RepositoryParser(ABC):
    """Abstract base class for a repository parser."""

    @abstractmethod
    def parse(self, repository_path: str) -> Generator[tuple[str, str], None, None]:
        """Parse the contents of a repository.

        Args:
            repository_url (str): The path of the repository to parse.

        Returns:
            str: The parsed contents of the repository.
        """
