from app.models.repository.models import RepositoryResponse
from app.services.abstract.database.VectorDBService import VectorDBService
from app.services.abstract.embedding.embedding_service import EmbeddingService
from app.services.abstract.repository.repository_parser import RepositoryParser
from app.services.abstract.repository.repository_service import RepositoryService


class RepositoryServiceImpl(RepositoryService):
    """Service implementation for handling repository-related operations."""

    def __init__(
        self, parser: RepositoryParser, embedding_service: EmbeddingService, vector_db_service: VectorDBService
    ):
        """Initialize the RepositoryServiceImpl with the given dependencies."""
        self.parser: RepositoryParser = parser
        self.embedding_service: EmbeddingService = embedding_service
        self.vector_db_service: VectorDBService = vector_db_service

    def process(self, repository_url: str) -> RepositoryResponse:
        """Parse the given repository URL and saves the parsed data and embedding vector to the database.

        Args:
            repository_url (str): The URL of the repository to process.

        Returns:
            RepositoryResponse: A response containing the processed repository data.
        """
        parsed_repository = self.parser.parse(repository_url)

        embedding_vector = self.embedding_service.encode(parsed_repository)

        self.vector_db_service.save(parsed_repository, embedding_vector, repository_url)

        return RepositoryResponse(
            repository_url=repository_url, parsed_repository=parsed_repository, embedding_vector=embedding_vector
        )
