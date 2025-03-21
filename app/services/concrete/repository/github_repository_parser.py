import os
import subprocess

from git import Repo

from app.config import settings
from app.services.abstract.repository.repository_parser import RepositoryParser


class GithubRepositoryParser(RepositoryParser):
    """Parse a GitHub repository into text."""

    def parse(self, repository_url: str) -> str:
        """Clone the repository and parses it into text.

        Args:
            repository_url (str): The URL of the repository to parse.

        Returns:
            str: The parsed contents of the repository.

        Raises:
            Exception: If the repository could not be parsed
        """
        try:
            if not os.path.exists(settings.REPO_CLONE_DIRECTORY):
                Repo.clone_from(repository_url, settings.REPO_CLONE_DIRECTORY)

            result = subprocess.run(
                ["repo-to-text", "--stdout"], cwd=settings.REPO_CLONE_DIRECTORY, capture_output=True, text=True
            )

            if result.returncode != 0:
                raise Exception(f"Failed to parse repository: {result.stderr}")

            with open("parsed_repo.txt", "w", encoding="utf-8") as f:
                f.write(result.stdout)

            return result.stdout
        except Exception as e:
            raise Exception(f"Failed to parse repository: {e}") from e
