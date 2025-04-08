import os
from typing import Generator

from app.services.abstract.repository.repository_parser import RepositoryParser


class RepositoryParserImpl(RepositoryParser):
    """Parse a repository into text."""

    def parse(self, repository_path: str) -> Generator[tuple[str, str], None, None]:
        """Parse the given repository path.

        Args:
            repository_path (str): The path of the repository to parse.

        Returns:
            Generator[tuple[str, str], None, None]: The parsed contents of the repository.

        Raises:
            Exception: If the repository could not be parsed
        """
        for root, _, files in os.walk(repository_path):
            for file in files:
                file_path: str = os.path.join(root, file)

                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content: str = f.read()
                        yield (file_path, content)
                except UnicodeDecodeError:
                    continue
