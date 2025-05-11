from fastapi import APIRouter, Depends, File, Form, UploadFile

from app.dependencies.document_dependencies import get_document_service
from app.exceptions.file_not_uploaded_error import FileNotUploadedError
from app.models.document.models import (
    DocumentQueryRequest,
    DocumentQueryResponse,
    DocumentUploadResponse,
)
from app.services.abstract.document.document_service import DocumentService

document_router: APIRouter = APIRouter(prefix="/document", tags=["Document"])


@document_router.post("/upload", response_model=DocumentUploadResponse)
async def upload_document(
    file: UploadFile = File(...), collection: str = Form(...), service: DocumentService = Depends(get_document_service)
) -> DocumentUploadResponse:
    """Upload document to temp directory and save to vectordb.

    Args:
        file (UploadFile): File to be upload
        collection (str): Collection that file will be save
        service (DocumentService): Inject DocumentService

    Raises:
        FileNotUploadedError: If errors happened

    Returns:
        DocumentUploadResponse: Response of document upload process
    """
    try:
        return await service.upload(file, collection)
    except Exception as e:
        raise FileNotUploadedError(f"{file.filename} {str(e)}")


@document_router.post("/query", response_model=DocumentQueryResponse)
async def query_repository(
    request: DocumentQueryRequest, service: DocumentService = Depends(get_document_service)
) -> DocumentQueryResponse:
    """Query the vectordb and ask to llm for relevant information based on the provided query.

    Args:
        request (QueryRequest): Contains the query string and other parameters.
        service (QueryService): Service instance that handles querying.

    Returns:
        QueryResponse: Answer of user query.
    """
    return await service.query(request)
