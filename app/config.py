from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """The environment variables used by the application."""

    EMBEDDING_MODEL_NAME: str = Field(description="Embedding model name")
    VECTOR_DB_PATH: str = Field(description="Path to the vector database")
    REPO_CLONE_DIRECTORY: str = Field(description="Path to the repository clone directory")


settings = Settings()
