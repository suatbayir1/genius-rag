from fastapi import APIRouter

from app.services.concrete.chunker.docling_chunker import DoclingChunker
from app.services.concrete.embedding.text_embedding import TextEmbedding

test_router: APIRouter = APIRouter(prefix="/test", tags=["test"])


@test_router.get("/parse-pdf")
def test() -> str:
    chunker = DoclingChunker()
    chunks = chunker.chunk("/Users/suatbayir/GENIUS/genius-rag/assets/Task-Planning.pdf")

    embedding_model = TextEmbedding()
    embedding_model.encode(chunks)

    return "API is working"
