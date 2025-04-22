from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """The environment variables used by the application."""

    EMBEDDING_MODEL_NAME: str = Field(description="Embedding model name")
    VECTOR_DB_PATH: str = Field(description="Path to the vector database")
    REPO_CLONE_DIRECTORY: str = Field(description="Path to the repository clone directory")
    VECTOR_DB_DEFAULT_DIMENSION: int = Field(description="Default dimension of the vector database")
    USE_GPU: bool = Field(description="Use GPU for processing")

    CHROMA_HOST: str = Field(description="ChromaDB host")
    CHROMA_PORT: int = Field(description="ChromaDB port")

    OLLAMA_BASE_URL: str = Field(description="Ollama base url")


settings = Settings()
