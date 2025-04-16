from fastapi import status

from app.exceptions.base import AppException


class UnsupportedTaskError(AppException):
    """Raised when an unsupported task is requested."""

    def __init__(self, task: str):
        """Initialize the exception with the unsupported task."""
        super().__init__(f"Unsupported task: {task}", status.HTTP_400_BAD_REQUEST)
