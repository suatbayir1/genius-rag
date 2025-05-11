from fastapi import status

from app.exceptions.base import AppException


class FileNotUploadedError(AppException):
    """Raised when an file not uplaoded."""

    def __init__(self, name: str):
        """Initialize the exception with the file not uploaded error."""
        super().__init__(f"File could not be uploaded: {name}", status.HTTP_422_UNPROCESSABLE_ENTITY)
