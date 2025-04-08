from unittest.mock import MagicMock

import pytest

from app.repositories.RepositoryRepository import RepositoryRepository
from app.services.abstract.language_detector import LanguageDetector
from app.services.abstract.llm.LLMService import LLMService
from app.services.abstract.repository.repository_cloner import RepositoryCloner
from app.services.abstract.repository.repository_parser import RepositoryParser
from app.services.concrete.repository.repository_service_impl import (
    RepositoryServiceImpl,
)


@pytest.fixture
def mock_repository_cloner() -> MagicMock:
    """Mock RepositoryCloner instance."""
    return MagicMock(spec=RepositoryCloner)


@pytest.fixture
def mock_language_detector() -> MagicMock:
    """Mock LanguageDetector instance."""
    return MagicMock(spec=LanguageDetector)


@pytest.fixture
def mock_repository_parser() -> MagicMock:
    """Mock RepositoryParser instance."""
    return MagicMock(spec=RepositoryParser)


@pytest.fixture
def mock_repository_repository() -> MagicMock:
    """Mock RepositoryRepository instance."""
    return MagicMock(spec=RepositoryRepository)


@pytest.fixture
def mock_llm_service() -> MagicMock:
    """Mock LLMService instance."""
    return MagicMock(spec=LLMService)


@pytest.fixture
def repository_service(
    mock_repository_cloner: MagicMock,
    mock_repository_parser: MagicMock,
    mock_language_detector: MagicMock,
    mock_repository_repository: MagicMock,
    mock_llm_service: MagicMock,
) -> RepositoryServiceImpl:
    """
    Fixture to provide an instance of RepositoryServiceImpl with mocked dependencies.

    Args:
        mock_repository_cloner: Mock of RepositoryCloner
        mock_repository_parser: Mock of RepositoryParser
        mock_language_detector: Mock of LanguageDetector
        mock_repository_repository: Mock of RepositoryRepository
        mock_llm_service: Mock of LLMService

    Returns:
        RepositoryServiceImpl: Instance of repository service with mocks.
    """
    return RepositoryServiceImpl(
        cloner=mock_repository_cloner,
        parser=mock_repository_parser,
        language_detector=mock_language_detector,
        repository=mock_repository_repository,
        llm_service=mock_llm_service,
    )
