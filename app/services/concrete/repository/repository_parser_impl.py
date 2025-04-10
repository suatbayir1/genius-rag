import os
from pathlib import Path
from typing import Generator

from app.constants import SUPPORTED_EXTENSIONS
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

                file_extension: str = Path(file_path).suffix

                if file_extension not in SUPPORTED_EXTENSIONS:
                    continue

                yield (file_path, file_extension)
