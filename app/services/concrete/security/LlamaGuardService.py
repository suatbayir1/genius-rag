import os

from transformers import pipeline

from app.config import settings
from app.services.abstract.security.GuardService import GuardService


class LlamaGuardService(GuardService):
    def __init__(self):
        """Initiate class."""
        model_path = os.path.join(settings.HF_MODEL_DIRECTORY, settings.TEXT_CLASSIFICATION_MODEL)
        self.pipe = pipeline(
            "text-classification", model=model_path, tokenizer=model_path, device=0 if settings.USE_GPU else -1
        )

    def is_safe_prompt(self, prompt: str) -> bool:
        """Check the prompt is safe.

        Args:
            prompt (str): User prompt

        Returns:
            bool: Safe or unsafe
        """
        result = self.pipe(prompt, truncation=True)[0]
        label = result["label"].lower()
        score = result["score"]

        if label == "toxic" and score > 0.7:
            return False
        return True
