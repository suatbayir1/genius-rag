from docling.document_converter import DocumentConverter
from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.services.abstract.chunking.chunker import Chunker


class DoclingChunker(Chunker):
    def __init__(self):
        """Initialize the DoclingChunker with a DocumentConverter and a text splitter."""
        self.converter = DocumentConverter()
        self.text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=200)

    def chunk(self, file_path: str) -> list[str]:
        """Split the text into chunks of specified size."""
        converted_document = self.converter.convert(file_path).document
        text = converted_document.export_to_markdown()

        chunks = self.text_splitter.split_text(text)
        return chunks
