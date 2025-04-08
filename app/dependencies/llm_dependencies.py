from app.services.abstract.llm.LLMService import LLMService
from app.services.concrete.llm.LangchainLLMService import LangchainLLMService


def get_llm_service() -> LLMService:
    """Return an implementation of LLMService."""
    return LangchainLLMService()
