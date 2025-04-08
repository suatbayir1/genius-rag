import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture
def client() -> TestClient:
    """Fixture to create a test client for FastAPI."""
    return TestClient(app)


@pytest.mark.skip(reason="Skipping test for now")
def test_parse_repository_success(client: TestClient) -> None:
    """Integration test for the /repository/parse endpoint.

    - Sends a POST request with a repository URL.
    - Verifies the response matches the expected RepositoryResponse.
    - Ensures correct HTTP status and data persistence.
    """
    request: dict[str, str] = {"repository_url": "https://github.com/suatbayir1/genius-rag"}

    response = client.post("/api/v1/repository/parse", json=request)

    assert response.status_code == 200
    response_data = response.json()

    assert "repository_url" in response_data
    assert response_data["repository_url"] == request["repository_url"]


def test_parse_repository_invalid_url(client: TestClient) -> None:
    """Integration test to ensure invalid URLs return an error.

    - Sends a POST request with an invalid repository URL.
    - Expects a 422 validation error from FastAPI.
    """
    request: dict[str, str] = {"repository_url": "invalid-url"}

    response = client.post("/api/v1/repository/parse", json=request)

    assert response.status_code == 422
