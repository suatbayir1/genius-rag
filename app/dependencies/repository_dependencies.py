from fastapi import Depends

from app.dependencies.database_dependencies import get_repository_repository
from app.dependencies.llm_dependencies import get_llm_service
from app.repositories.RepositoryRepository import RepositoryRepository
from app.services.abstract.language_detector import LanguageDetector
from app.services.abstract.llm.llm_service import LLMService
from app.services.abstract.repository.repository_cloner import RepositoryCloner
from app.services.abstract.repository.repository_parser import RepositoryParser
from app.services.abstract.repository.repository_service import RepositoryService
from app.services.concrete.pygments_language_detectory import PygmentsLanguageDetector
from app.services.concrete.repository.repository_cloner_impl import RepositoryClonerImpl
from app.services.concrete.repository.repository_parser_impl import RepositoryParserImpl
from app.services.concrete.repository.repository_service_impl import (
    RepositoryServiceImpl,
)


def get_repository_cloner() -> RepositoryCloner:
    """Return an instance of RepositoryClonerImpl, implementing the RepositoryCloner interface."""
    return RepositoryClonerImpl()


def get_language_detector() -> LanguageDetector:
    """Return an instance of PygmentsLanguageDetector, implementing the LanguageDetector interface."""
    return PygmentsLanguageDetector()


def get_repository_parser() -> RepositoryParser:
    """Return an instance of RepositoryParserImpl, implementing the RepositoryParser interface."""
    return RepositoryParserImpl()


def get_repository_service(
    cloner: RepositoryCloner = Depends(get_repository_cloner),
    parser: RepositoryParser = Depends(get_repository_parser),
    language_detector: LanguageDetector = Depends(get_language_detector),
    repository: RepositoryRepository = Depends(get_repository_repository),
    llm_service: LLMService = Depends(get_llm_service),
) -> RepositoryService:
    """Return an instance of RepositoryServiceImpl, implementing the RepositoryService interface.

    Args:
        cloner (RepositoryCloner): Clones repository from URL.
        parser (RepositoryParser): Parses repository-related data.
        language_detector (LanguageDetector): Detects programming language of files.
        repository (RepositoryRepository): Manages vector-based storage and retrieval.

    Returns:
        RepositoryService: An instance of RepositoryServiceImpl with dependencies injected.
    """
    return RepositoryServiceImpl(cloner, parser, language_detector, repository, llm_service)
