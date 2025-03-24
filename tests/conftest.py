from unittest.mock import MagicMock

import pytest

from app.repositories.RepositoryRepository import RepositoryRepository
from app.services.abstract.embedding.embedding_service import EmbeddingService
from app.services.abstract.repository.repository_parser import RepositoryParser
from app.services.concrete.repository.repository_service_impl import (
    RepositoryServiceImpl,
)


@pytest.fixture
def mock_repository_parser() -> MagicMock:
    """Mock RepositoryParser instance."""
    return MagicMock(spec=RepositoryParser)


@pytest.fixture
def mock_embedding_service() -> MagicMock:
    """Mock EmbeddingService instance."""
    return MagicMock(spec=EmbeddingService)


@pytest.fixture
def mock_repository_repository() -> MagicMock:
    """Mock RepositoryRepository instance."""
    return MagicMock(spec=RepositoryRepository)


@pytest.fixture
def repository_service(
    mock_repository_parser: MagicMock, mock_embedding_service: MagicMock, mock_repository_repository: MagicMock
) -> RepositoryServiceImpl:
    """
    Fixture to provide an instance of RepositoryServiceImpl with mocked dependencies.

    Args:
        mock_repository_parser: Mock of RepositoryParser
        mock_embedding_service: Mock of EmbeddingService
        mock_repository_repository: Mock of RepositoryRepository

    Returns:
        RepositoryServiceImpl: Instance of repository service with mocks.
    """
    return RepositoryServiceImpl(
        parser=mock_repository_parser,
        embedding_service=mock_embedding_service,
        repository=mock_repository_repository,
    )
