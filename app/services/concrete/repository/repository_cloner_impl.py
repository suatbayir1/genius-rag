import tempfile

from git import Repo
from pydantic import HttpUrl

from app.services.abstract.repository.repository_cloner import RepositoryCloner


class RepositoryClonerImpl(RepositoryCloner):
    def clone(self, repository_url: HttpUrl) -> str:
        """Return the path to the cloned repository.

        Args:
            repository_url (HttpUrl): The URL of the repository to clone.
        """
        temp_dir = tempfile.mkdtemp()
        Repo.clone_from(repository_url, temp_dir)
        return temp_dir
