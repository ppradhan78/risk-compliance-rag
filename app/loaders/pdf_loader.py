from pathlib import Path

from pypdf import PdfReader

from app.loaders.base import Document


def load_pdf(file_path: str) -> list[Document]:

    documents = []

    reader = PdfReader(file_path)

    for page_number, page in enumerate(reader.pages, start=1):

        text = page.extract_text() or ""

        if not text.strip():
            continue

        documents.append(
            Document(
                text=text,
                metadata={
                    "document_name": Path(file_path).name,
                    "file_type": "pdf",
                    "page_number": page_number
                }
            )
        )

    return documents