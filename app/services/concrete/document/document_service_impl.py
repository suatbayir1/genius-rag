import shutil
from pathlib import Path
from typing import Any, Dict, List

from fastapi import UploadFile
from langchain.schema.document import Document

from app.config import settings
from app.domain.filtering.sequential_dropoff import SequentialDropOffFilter
from app.factories.chunker_factory import ChunkerFactory
from app.factories.embedding_model_factory import EmbeddingModelFactory
from app.factories.task_handler_factory import TaskHandlerFactory
from app.models.document.models import (
    DocumentChunk,
    DocumentQueryRequest,
    DocumentQueryResponse,
    DocumentUploadResponse,
)
from app.models.llm.enums import LLMTaskType
from app.repositories.document_repository import DocumentRepository
from app.services.abstract.document.document_service import DocumentService
from app.services.abstract.embedding.embedding import Embedding
from app.services.abstract.llm.llm_service import LLMService
from app.services.abstract.llm.task_handler import TaskHandler
from app.services.abstract.security.GuardService import GuardService
from app.services.concrete.embedding.ollama_embedding import OllamaEmbedding
from app.utils.logger import get_logger
from app.utils.responses import ResponseMessage

logger = get_logger(__name__)


class DocumentServiceImpl(DocumentService):
    def __init__(self, repository: DocumentRepository, llm_service: LLMService, guard_service: GuardService) -> None:
        """Manage document operations.

        Args:
            repository (DocumentRepository): Document repository
            llm_service (LLMService): LLM service
            guard_service (GuardService): Guard service
        """
        self.repository: DocumentRepository = repository
        self.llm_service: LLMService = llm_service
        self.guard_service: GuardService = guard_service

    async def save(self, file: UploadFile) -> str:
        """Save file in directory.

        Args:
            file (UploadFile): File to be save

        Returns:
            str: File path
        """
        upload_dir = Path(settings.UPLOAD_DIR)
        upload_dir.mkdir(exist_ok=True)

        file_path = upload_dir / file.filename

        if file_path.exists():
            raise FileExistsError(f"File '{file.filename}' already exists.")

        with open(file_path, "wb") as f:
            shutil.copyfileobj(file.file, f)

        return str(file_path)

    async def upload(self, file: UploadFile, collection_name: str) -> DocumentUploadResponse:
        """Save file to vectordb.

        Args:
            file (UploadFile): File to be upload
            collection_name (str): Collection name

        Returns:
            DocumentUploadResponse: Response of upload document process
        """
        file_path: str = await self.save(file)

        extension: str = Path(file_path).suffix
        chunks: list[Document] = ChunkerFactory.get_chunker(extension).chunk(file_path)

        # Get existing ids
        existing_ids: set = self.repository.get_existing_ids(collection_name)

        # Only add documents that don't exist in the DB.
        new_chunks: List[Document] = []
        for chunk in chunks:
            if chunk.metadata["id"] not in existing_ids:
                new_chunks.append(chunk)

        if not new_chunks:
            logger.info("No new chunks to add..")
            return DocumentUploadResponse(message=ResponseMessage.FILE_ALREADY_UPLOADED)

        new_chunk_ids: list[str] = [chunk.metadata["id"] for chunk in new_chunks]
        documents_text: list[str] = [chunk.page_content for chunk in new_chunks]
        metadatas: list[dict[str, Any]] = [chunk.metadata for chunk in new_chunks]

        embedding_model: Embedding = EmbeddingModelFactory.get_embedding(OllamaEmbedding)
        embeddings: List[List[float]] = embedding_model.encode(documents_text)

        self.repository.save(collection_name, new_chunk_ids, documents_text, embeddings, metadatas)
        return DocumentUploadResponse(message=ResponseMessage.FILE_UPLOAD_SUCCESS)

    async def query(self, request: DocumentQueryRequest) -> DocumentQueryResponse:
        """Query to llm using vectordb.

        Args:
            request (DocumentQueryRequest): Request payload

        Returns:
            DocumentQueryResponse: _description_
        """
        if not self.guard_service.is_safe_prompt(request.query):
            return DocumentQueryResponse(response=ResponseMessage.INVALID_PROMPT, sources=[])

        embedding_model: Embedding = EmbeddingModelFactory.get_embedding(OllamaEmbedding)
        query_embeddings: List[List[float]] = embedding_model.encode([request.query])

        results: Dict[str, Any] = self.repository.query(
            collection_name=request.collection,
            query_embeddings=query_embeddings,
            top_k=request.top_k,
        )

        documents = results.get("documents", [[]])[0]
        metadatas = results.get("metadatas", [[]])[0]
        distances = results.get("distances", [[]])[0]

        filter_strategy = SequentialDropOffFilter()
        filtered_docs, filtered_meta, filtered_scores = filter_strategy.filter(documents, metadatas, distances)

        context_text = "\n\n---\n\n".join(filtered_docs)
        sources: List[DocumentChunk] = []
        for doc, meta, score in zip(filtered_docs, filtered_meta, filtered_scores):
            sources.append(DocumentChunk(id=meta.get("id"), text=doc, score=score))

        handler: TaskHandler = TaskHandlerFactory(self.llm_service).get_handler(LLMTaskType.QA)
        answer: str = handler.handle(context=context_text, query=request.query)

        if not self.guard_service.is_safe_prompt(answer):
            return DocumentQueryResponse(response=ResponseMessage.INVALID_RESPONSE, sources=[])

        return DocumentQueryResponse(response=answer, sources=sources)
