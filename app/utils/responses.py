from enum import Enum


class ResponseMessage(str, Enum):
    FILE_UPLOAD_SUCCESS = "File uploaded successfully."
    FILE_ALREADY_UPLOADED = "File already uploaded."
