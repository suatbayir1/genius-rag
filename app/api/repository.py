from fastapi import APIRouter, Depends

from app.dependencies.repository_dependencies import get_repository_service
from app.models.repository.models import (
    QueryRequest,
    QueryResponse,
    RepositoryRequest,
    RepositoryResponse,
)
from app.services.abstract.repository.repository_service import RepositoryService

repository_router: APIRouter = APIRouter(prefix="/repository", tags=["Repository"])


@repository_router.post("/parse", response_model=RepositoryResponse)
def parse_repository(
    repository_request: RepositoryRequest, service: RepositoryService = Depends(get_repository_service)
) -> RepositoryResponse:
    """Parse the given repository URL and saves the parsed data and embedding vector to the database.

    Args:
        repository_request (RepositoryRequest): Contains the repository URL to be parsed.
        service (RepositoryService, optional): Service instance that handles repository parsing.

    Returns:
        RepositoryResponse: Response containing processed repository data.
    """
    return service.process(repository_request.repository_url)


@repository_router.post("/query", response_model=QueryResponse)
def query_repository(
    request: QueryRequest, service: RepositoryService = Depends(get_repository_service)
) -> QueryResponse:
    """Query the repository for relevant information based on the provided query.

    Args:
        request (QueryRequest): Contains the query string and other parameters.
        service (RepositoryService): Service instance that handles repository querying.

    Returns:
        QueryResponse: List of the most relevant stored documents.
    """
    return service.query(request)
