from fastapi import Depends

from app.dependencies.database_dependencies import get_vector_db_service
from app.dependencies.embedding_dependencies import get_embedding_service
from app.services.abstract.database.VectorDBService import VectorDBService
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
    vector_db_service: VectorDBService = Depends(get_vector_db_service),
) -> RepositoryService:
    """Return an instance of RepositoryServiceImpl, implementing the RepositoryService interface.

    Args:
        parser (RepositoryParser): Parses repository-related data.
        embedding_service (EmbeddingService): Handles text embeddings.
        vector_db_service (VectorDBService): Manages vector-based storage and retrieval.

    Returns:
        RepositoryService: An instance of RepositoryServiceImpl with dependencies injected.
    """
    return RepositoryServiceImpl(parser, embedding_service, vector_db_service)
