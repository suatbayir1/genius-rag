from fastapi import Depends

from app.dependencies.database_dependencies import get_document_repository
from app.dependencies.llm_dependencies import get_document_llm_service
from app.repositories.document_repository import DocumentRepository
from app.services.abstract.document.document_service import DocumentService
from app.services.abstract.llm.llm_service import LLMService
from app.services.abstract.security.GuardService import GuardService
from app.services.concrete.document.document_service_impl import DocumentServiceImpl
from app.services.concrete.security.LlamaGuardService import LlamaGuardService


def get_guard_service() -> GuardService:
    """Return an instance of LlamaGuardService, implementing the GuardService interface."""
    return LlamaGuardService()


def get_document_service(
    repository: DocumentRepository = Depends(get_document_repository),
    llm_service: LLMService = Depends(get_document_llm_service),
    guard_service: GuardService = Depends(get_guard_service),
) -> DocumentService:
    """Return an instance of DocumentServiceImpl, implementing the DocumentService interface."""
    return DocumentServiceImpl(repository, llm_service, guard_service)
