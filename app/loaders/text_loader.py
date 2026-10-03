from pathlib import Path

from app.loaders.base import Document


def load_text(file_path: str) -> list[Document]:

    path = Path(file_path)

    text = path.read_text(
        encoding="utf-8"
    )

    return [
        Document(
            text=text,
            metadata={
                "document_name": path.name,
                "file_type": "txt"
            }
        )
    ]