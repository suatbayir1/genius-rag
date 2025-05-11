from abc import ABC, abstractmethod

from fastapi import UploadFile

from app.models.document.models import (
    DocumentQueryRequest,
    DocumentQueryResponse,
    DocumentUploadResponse,
)


class DocumentService(ABC):
    """Abstract base class for document service."""

    @abstractmethod
    async def upload(self, file: UploadFile, collection: str) -> DocumentUploadResponse:
        """Save the uploaded file to disk and return its path."""

    @abstractmethod
    async def query(self, request: DocumentQueryRequest) -> DocumentQueryResponse:
        """Query vectordb and ask to llm using user query."""
