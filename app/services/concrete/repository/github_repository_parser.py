import subprocess
import tempfile

from git import Repo

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
            with tempfile.TemporaryDirectory() as temp_dir:
                Repo.clone_from(repository_url, temp_dir)

                result = subprocess.run(["repo-to-text", "--stdout"], cwd=temp_dir, capture_output=True, text=True)

                if result.returncode != 0:
                    raise Exception(f"Failed to parse repository: {result.stderr}")

                return result.stdout
        except Exception as e:
            raise Exception(f"Failed to parse repository: {e}") from e
