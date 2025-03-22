from fastapi import Depends

from app.dependencies.database_dependencies import get_repository_repository
from app.dependencies.embedding_dependencies import get_embedding_service
from app.repositories.RepositoryRepository import RepositoryRepository
from app.services.abstract.embedding.embedding_service import EmbeddingService
from app.services.abstract.repository.repository_parser import RepositoryParser
from app.services.abstract.repository.repository_service import RepositoryService
from app.services.concrete.repository.github_repository_parser import (
    GithubRepositoryParser,
)
from app.services.concrete.repository.repository_service_impl import (
    RepositoryServiceImpl,
)


def get_repository_parser() -> RepositoryParser:
    """Return an instance of GithubRepositoryParser, implementing the RepositoryParser interface."""
    return GithubRepositoryParser()


def get_repository_service(
    parser: RepositoryParser = Depends(get_repository_parser),
    embedding_service: EmbeddingService = Depends(get_embedding_service),
    repository: RepositoryRepository = Depends(get_repository_repository),
) -> RepositoryService:
    """Return an instance of RepositoryServiceImpl, implementing the RepositoryService interface.

    Args:
        parser (RepositoryParser): Parses repository-related data.
        embedding_service (EmbeddingService): Handles text embeddings.
        repository (RepositoryRepository): Manages vector-based storage and retrieval.

    Returns:
        RepositoryService: An instance of RepositoryServiceImpl with dependencies injected.
    """
    return RepositoryServiceImpl(parser, embedding_service, repository)
