from fastapi import APIRouter

from app.rag.service import RAGService
from app.ingestion.pipeline import IngestionPipeline


router = APIRouter()

rag_service = RAGService()

ingestion_pipeline = (
    IngestionPipeline()
)


@router.post("/ingest")
def ingest_document(
    file_path: str,
    document_type: str
):

    count = (
        ingestion_pipeline
        .ingest_pdf(
            file_path,
            document_type
        )
    )

    return {
        "status": "success",
        "chunks_created": count
    }


@router.post("/search")
def search(
    query: str,
    top_k: int = 5
):

    results = (
        rag_service
        .retrieve_context(
            query,
            top_k
        )
    )

    return {
        "query": query,
        "results": results
    }