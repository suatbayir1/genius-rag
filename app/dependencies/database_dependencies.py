from app.services.abstract.database.VectorDBService import VectorDBService
from app.services.concrete.database.ChromaDBService import ChromaDBService


def get_vector_db_service() -> VectorDBService:
    """Return an instance of ChromaDBService, implementing the VectorDBService interface."""
    return ChromaDBService()
