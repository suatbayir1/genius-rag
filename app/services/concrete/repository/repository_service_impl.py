from pydantic import HttpUrl

from app.models.repository.models import RepositoryResponse
from app.repositories.RepositoryRepository import RepositoryRepository
from app.services.abstract.embedding.embedding_service import EmbeddingService
from app.services.abstract.repository.repository_parser import RepositoryParser
from app.services.abstract.repository.repository_service import RepositoryService


class RepositoryServiceImpl(RepositoryService):
    """Service implementation for handling repository-related operations."""

    def __init__(self, parser: RepositoryParser, embedding_service: EmbeddingService, repository: RepositoryRepository):
        """Initialize the RepositoryServiceImpl with the given dependencies."""
        self.parser: RepositoryParser = parser
        self.embedding_service: EmbeddingService = embedding_service
        self.repository: RepositoryRepository = repository

    def process(self, repository_url: HttpUrl) -> RepositoryResponse:
        """Parse the given repository URL and saves the parsed data and embedding vector to the database.

        Args:
            repository_url (HttpUrl): The URL of the repository to process.

        Returns:
            RepositoryResponse: A response containing the processed repository data.
        """
        parsed_repository = self.parser.parse(repository_url)

        embedding_vector = self.embedding_service.encode(parsed_repository)

        self.repository.save(parsed_repository, embedding_vector, str(repository_url))

        return RepositoryResponse(repository_url=repository_url)
