from enum import Enum


class ResponseMessage(str, Enum):
    FILE_UPLOAD_SUCCESS = "File uploaded successfully."
    FILE_ALREADY_UPLOADED = "File already uploaded."

    INVALID_PROMPT = "🚫 This query does not comply with our security policies."
    INVALID_RESPONSE = "🚫 We cannot produce an answer to this question.."
