import uuid

from qdrant_client.models import PointStruct

from app.loaders.pdf_loader import load_pdf
from app.ingestion.cleaner import clean_text
from app.ingestion.chunker import chunk_text
from app.embeddings.service import EmbeddingService
from app.vectorstore.qdrant_store import QdrantStore


class IngestionPipeline:

    def __init__(self):

        self.embedding_service = (
            EmbeddingService()
        )

        self.vector_store = (
            QdrantStore()
        )

    def ingest_pdf(
        self,
        file_path: str,
        document_type: str
    ):

        documents = load_pdf(
            file_path
        )

        points = []

        for document in documents:

            cleaned_text = clean_text(
                document.text
            )

            chunks = chunk_text(
                cleaned_text
            )

            embeddings = (
                self.embedding_service
                .embed_documents(chunks)
            )

            for index, (
                chunk,
                embedding
            ) in enumerate(
                zip(chunks, embeddings)
            ):

                payload = {
                    **document.metadata,

                    "document_type":
                        document_type,

                    "chunk_id":
                        index,

                    "text":
                        chunk
                }

                points.append(
                    PointStruct(
                        id=str(uuid.uuid4()),
                        vector=embedding,
                        payload=payload
                    )
                )

        self.vector_store.upsert(
            points
        )

        return len(points)