from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """The environment variables used by the application."""

    EMBEDDING_MODEL_NAME: str = Field(description="Embedding model name")
    USE_GPU: bool = Field(description="Use GPU for processing")
    UPLOAD_DIR: str = Field(description="Upload directory path")

    CHROMA_HOST: str = Field(description="ChromaDB host")
    CHROMA_PORT: int = Field(default=8000, description="ChromaDB port")

    OLLAMA_BASE_URL: str = Field(description="Ollama base url")

    HF_MODEL_DIRECTORY: str = Field(description="Model directory")
    DOCLING_MODEL_DIRECTORY: str = Field(description="Docling model directory")
    CODE_EMBEDDING_MODEL: str = Field(description="Embedding model name for code")
    TEXT_EMBEDDING_MODEL: str = Field(description="Embedding model name for text")


settings = Settings()
