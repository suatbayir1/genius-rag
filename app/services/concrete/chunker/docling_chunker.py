from typing import List

from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import (
    EasyOcrOptions,
    PdfPipelineOptions,
    TableStructureOptions,
    smolvlm_picture_description,
)
from docling.document_converter import DocumentConverter, PdfFormatOption
from docling_core.types.doc import DoclingDocument
from langchain.schema.document import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.config import settings
from app.services.abstract.chunking.chunker import Chunker

CHUNK_SIZE: int = 800
CHUNK_OVERLAP: int = 80
IMAGE_PLACEHOLDER = "<!-- image_placeholder -->"
PAGE_BREAK_PLACEHOLDER = "<!-- page_break_ -->"


class DoclingChunker(Chunker):
    def __init__(self):
        """Initialize the DoclingChunker with a DocumentConverter and a text splitter."""
        pipeline_options = PdfPipelineOptions(
            artifacts_path=settings.DOCLING_MODEL_DIRECTORY,
            generate_page_images=True,
            images_scale=1.00,
            do_ocr=True,
            do_picture_description=True,
            ocr_options=EasyOcrOptions(),
            picture_description_options=smolvlm_picture_description,
            do_table_structure=True,
            table_structure_options=TableStructureOptions(do_cell_matching=True),
        )

        format_options = {InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)}

        self.converter = DocumentConverter(format_options=format_options)

        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP, length_function=len, is_separator_regex=False
        )

    def chunk(self, file_path: str) -> list[str]:
        """Parse the pdf using docling.

        Args:
            file_path (str): File path of file to be parsed

        Returns:
            list[str]: List of chunks of file
        """
        document: DoclingDocument = self.converter.convert(file_path).document
        markdown: str = document.export_to_markdown(
            page_break_placeholder=PAGE_BREAK_PLACEHOLDER, image_placeholder=IMAGE_PLACEHOLDER
        )

        # Process image annotations
        annotations: list[str] = self.get_annotations(document)
        markdown_with_figures: str = self.replace_occurrences(markdown, IMAGE_PLACEHOLDER, annotations)

        pages: list[str] = markdown_with_figures.split(PAGE_BREAK_PLACEHOLDER)
        all_chunks: list[Document] = []

        for page_number, page_markdown in enumerate(pages, start=1):
            chunks = self.splitter.split_text(page_markdown)

            for chunk_id, chunk in enumerate(chunks, start=1):
                all_chunks.append(
                    Document(
                        page_content=chunk,
                        metadata={"source": file_path, "id": f"{file_path}:{page_number}:{chunk_id}"},
                    )
                )

        return all_chunks

    def get_annotations(self, document: DoclingDocument) -> list[str]:
        """Find the annotations of pictures.

        Args:
            document (DoclingDocument): Docling document

        Returns:
            list[str]: List of annotations of pictures
        """
        annotations = []

        for picture in document.pictures:
            # leave empty if there is no annotation of the picture
            if not picture.annotations:
                annotations.append("")

            for annotation in picture.annotations:
                annotations.append(annotation.text)

        return annotations

    def replace_occurrences(self, text: str, target: str, replacements: List[str]) -> str:
        """Replace picture placeholders with annotations.

        Args:
            text (str): Annotation of picture
            target (str): Picture placeholder
            replacements (str): Replacements

        Raises:
            ValueError: If no more occurences

        Returns:
            str: Replaced text
        """
        for replacement in replacements:
            if target in text:
                text = text.replace(target, replacement, 1)
            else:
                raise ValueError("No more occurrences..")

        return text
