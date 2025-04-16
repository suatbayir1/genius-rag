from fastapi import status


class AppException(Exception):
    """Base exception class for the application."""

    def __init__(self, message: str, status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR):
        """Initialize the exception with a message and status code.

        Args:
            message (str): The error message.
            status_code (int): The HTTP status code.
        """
        super().__init__(message)
        self.message = message
        self.status_code = status_code
