from abc import ABC, abstractmethod

from pydantic import HttpUrl


class RepositoryCloner(ABC):
    @abstractmethod
    def clone(self, repository_url: HttpUrl) -> str:
        """Return the path to the cloned repository.

        Args:
            repository_url (HttpUrl): The URL of the repository to clone.
        """
