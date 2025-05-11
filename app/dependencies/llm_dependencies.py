from app.services.abstract.llm.llm_service import LLMService
from app.services.concrete.llm.langchain_llm_service import LangchainLLMService


def get_llm_service(model_name: str = "llama3.2") -> LLMService:
    """Return an implementation of LLMService."""
    return LangchainLLMService(model_name)


def get_document_llm_service() -> LLMService:
    """Return an implementation of LLMService."""
    return get_llm_service(model_name="mistral")
