import uuid
from typing import Any, Dict, List, Optional

from pydantic import HttpUrl

from app.exceptions.unsupported_task_exception import UnsupportedTaskError
from app.factories.chunker_factory import ChunkerFactory
from app.factories.embedding_model_factory import EmbeddingModelFactory
from app.factories.task_handler_factory import TaskHandlerFactory
from app.models.llm.enums import LLMTaskType
from app.models.repository.models import QueryRequest, QueryResponse, RepositoryResponse
from app.repositories.RepositoryRepository import RepositoryRepository
from app.services.abstract.chunking.chunker import Chunker
from app.services.abstract.embedding.embedding import Embedding
from app.services.abstract.language_detector import LanguageDetector
from app.services.abstract.llm.llm_service import LLMService
from app.services.abstract.llm.task_handler import TaskHandler
from app.services.abstract.repository.repository_cloner import RepositoryCloner
from app.services.abstract.repository.repository_parser import RepositoryParser
from app.services.abstract.repository.repository_service import RepositoryService

BATCH_SIZE = 10


class RepositoryServiceImpl(RepositoryService):
    """Service implementation for handling repository-related operations."""

    def __init__(
        self,
        cloner: RepositoryCloner,
        parser: RepositoryParser,
        language_detector: LanguageDetector,
        repository: RepositoryRepository,
        llm_service: LLMService,
    ):
        """Initialize the RepositoryServiceImpl with the given dependencies."""
        self.cloner: RepositoryCloner = cloner
        self.parser: RepositoryParser = parser
        self.language_detector: LanguageDetector = language_detector
        self.repository: RepositoryRepository = repository
        self.llm_service: LLMService = llm_service
        self.task_handler_factory: TaskHandlerFactory = TaskHandlerFactory(llm_service)

    def process(self, repository_url: HttpUrl) -> RepositoryResponse:
        """Parse the given repository URL and saves the parsed data and embedding vector to the database.

        Args:
            repository_url (HttpUrl): The URL of the repository to process.

        Returns:
            RepositoryResponse: A response containing the processed repository data.
        """
        repository_path: str = self.cloner.clone(repository_url)

        parsed_files = self.parser.parse(repository_path)

        for file_path, file_extension in parsed_files:
            chunker: Chunker = ChunkerFactory.get_chunker(file_extension)
            chunks = chunker.chunk(file_path)

            if not chunks:
                continue

            embedding_model: Embedding = EmbeddingModelFactory.get_embedding_model(file_extension)
            embeddings: List[float] = embedding_model.encode(chunks)

            doc_ids: List[str] = [str(uuid.uuid4()) for _ in range(len(embeddings))]
            metadatas: List[dict[str, Any]] = [{"text": chunk, "file_path": file_path} for chunk in chunks]

            collection_name: str = embedding_model.__class__.__name__
            self.repository.save(collection_name, doc_ids, chunks, embeddings, metadatas)

        return RepositoryResponse(repository_url=repository_url)

    def query(self, request: QueryRequest) -> QueryResponse:
        """Query the vector database with either code or text.

        Args:
            request (QueryRequest): Contains the query string and other parameters.

        Returns:
            QueryResponse: List of the most relevant stored documents.
        """
        query_type_handler: TaskHandler = self.task_handler_factory.get_handler(LLMTaskType.DETECT_QUERY_TYPE)
        llm_response: str = query_type_handler.handle(
            context=LLMTaskType.to_prompt_list(exclude={LLMTaskType.DETECT_QUERY_TYPE}), query=request.query
        )
        task_type: Optional[LLMTaskType] = LLMTaskType.from_llm_output(llm_response)

        if not task_type:
            raise UnsupportedTaskError(str(task_type))

        embedding_model: Embedding = EmbeddingModelFactory.get_embedding(task_type.embedding_model_class)
        query_embeddings: List[float] = embedding_model.encode([request.query])
        collection_name: str = embedding_model.__class__.__name__

        results: Dict[str, Any] = self.repository.query(
            collection_name=collection_name,
            query_embeddings=query_embeddings,
            top_k=request.top_k,
        )

        handler: TaskHandler = self.task_handler_factory.get_handler(task_type)
        answer: str = handler.handle(context=results["metadatas"], query=request.query)

        return QueryResponse(documents={"answer": answer})
