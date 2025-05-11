from app.repositories.document.chromadb_document_repository import (
    ChromaDBDocumentRepository,
)
from app.repositories.document_repository import DocumentRepository
from app.repositories.repository.ChromaDBRepositoryRepository import (
    ChromaDBRepositoryRepository,
)
from app.repositories.RepositoryRepository import RepositoryRepository


def get_repository_repository() -> RepositoryRepository:
    """Return an instance of ChromaDBRepositoryRepository, implementing the Repository interface."""
    return ChromaDBRepositoryRepository()


def get_document_repository() -> DocumentRepository:
    """Return an instance of ChromaDBRepositoryRepository, implementing the DocumentRepository interface."""
    return ChromaDBDocumentRepository()
