from pygments.lexers import guess_lexer, guess_lexer_for_filename
from pygments.util import ClassNotFound

from app.services.abstract.language_detector import LanguageDetector


class PygmentsLanguageDetector(LanguageDetector):
    """Implementation of a language detector using Pygments."""

    def detect(self, file_path: str, content: str) -> str:
        """Detect the language of a text using Pygments.

        Args:
            file_path (str): Extension based detection.
            content (str): Content of the file.

        Returns:
            Optional[str]: The detected language of the text.
        """
        try:
            lexer = guess_lexer_for_filename(file_path, content)
            return lexer.name.lower()
        except ClassNotFound:
            return "Text"

    def is_code(self, query: str) -> bool:
        try:
            guess_lexer(query)
            return True
        except ClassNotFound:
            return False
