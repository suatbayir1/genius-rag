from app.services.abstract.llm.llm_service import LLMService
from app.services.concrete.llm.langchain_llm_service import LangchainLLMService


def get_llm_service() -> LLMService:
    """Return an implementation of LLMService."""
    return LangchainLLMService()
