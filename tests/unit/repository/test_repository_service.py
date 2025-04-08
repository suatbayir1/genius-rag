from unittest.mock import MagicMock

import pytest
from pydantic import HttpUrl

from app.services.concrete.repository.repository_service_impl import (
    RepositoryServiceImpl,
)


@pytest.mark.skip(reason="Skipping test for now")
def test_process_repository(
    repository_service: RepositoryServiceImpl,
    mock_repository_parser: MagicMock,
    mock_embedding_service: MagicMock,
    mock_repository_repository: MagicMock,
) -> None:
    """
    Test the process method of RepositoryServiceImpl.

    This test ensures that:
    - The repository URL is correctly processed.
    - The repository is parsed into text.
    - The parsed text is encoded into an embedding vector.
    - The parsed repository and its embedding are stored correctly.

    Args:
        repository_service: Instance of RepositoryServiceImpl (with mocked dependencies).
        mock_repository_parser: Mocked RepositoryParser instance.
        mock_embedding_service: Mocked EmbeddingService instance.
        mock_repository_repository: Mocked RepositoryRepository instance.
    """
    repo_url = HttpUrl("https://github.com/suatbayir1/genius-rag")

    mock_repository_parser.parse.return_value = "parsed content"
    mock_embedding_service.encode.return_value = [0.1, 0.2, 0.3]

    response = repository_service.process(repo_url)

    assert response.repository_url == repo_url

    mock_repository_parser.parse.assert_called_once_with(repo_url)
    mock_embedding_service.encode.assert_called_once_with("parsed content")
    mock_repository_repository.save.assert_called_once()
