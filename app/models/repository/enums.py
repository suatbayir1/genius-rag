from enum import Enum


class Language(Enum):
    """Enum for programming languages."""

    PYTHON = ".py"

    @classmethod
    def is_valid(cls, language: str) -> bool:
        """Check if the given language is valid."""
        if not language:
            return False
        return language in cls._value2member_map_
