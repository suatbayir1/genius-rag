from app.repositories.repository.ChromaDBRepositoryRepository import (
    ChromaDBRepositoryRepository,
)
from app.repositories.RepositoryRepository import RepositoryRepository


def get_repository_repository() -> RepositoryRepository:
    """Return an instance of ChromaDBRepositoryRepository, implementing the Repository interface."""
    return ChromaDBRepositoryRepository()
