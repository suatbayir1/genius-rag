from pydantic import BaseModel, Field


class DocumentUploadResponse(BaseModel):
    """Response model for document upload."""

    message: str = Field(..., description="Document upload response message")


class DocumentQueryRequest(BaseModel):
    """Request model for repository querying."""

    query: str = Field(..., description="Query string")
    top_k: int = Field(5, description="Number of top results to return")
    collection: str = Field(..., description="Collection name to be querying.")


class DocumentChunk(BaseModel):
    """Response model for document chunk."""

    id: str = Field(..., description="Id of related chunk")
    text: str = Field(..., description="Text of related chunk")
    score: int = Field(..., description="Similarity percentege as int")


class DocumentQueryResponse(BaseModel):
    """Response model for querying."""

    response: str = Field(..., description="Response of user query from llm")
    sources: list[DocumentChunk] = Field(..., description="Most relevant sources for user query from vectordb")
