from abc import ABC, abstractmethod


class LanguageDetector(ABC):
    """Abstract base class for a language detector."""

    @abstractmethod
    def detect(self, file_path: str, content: str) -> str:
        """Detect the language of a text.

        Args:
            file_path (str): Extension based detection.
            content (str): Content of the file.

        Returns:
            Optional[str]: The detected language of the text.
        """

    @abstractmethod
    def is_code(self, query: str) -> bool:
        """Check if the query is code.

        Args:
            query (str): The query to check.

        Returns:
            bool: True if the query is code, False otherwise.
        """
