from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """The environment variables used by the application."""

    EMBEDDING_MODEL_NAME: str = Field(description="Embedding model name")
    USE_GPU: bool = Field(description="Use GPU for processing")

    CHROMA_HOST: str = Field(description="ChromaDB host")
    CHROMA_PORT: int = Field(description="ChromaDB port")

    OLLAMA_BASE_URL: str = Field(description="Ollama base url")


settings = Settings()
