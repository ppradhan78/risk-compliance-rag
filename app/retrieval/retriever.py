from app.embeddings.service import EmbeddingService
from app.vectorstore.qdrant_store import QdrantStore


class Retriever:

    def __init__(self):

        self.embedding_service = (
            EmbeddingService()
        )

        self.vector_store = (
            QdrantStore()
        )

    def retrieve(
        self,
        query: str,
        top_k: int = 5
    ):

        query_vector = (
            self.embedding_service
            .embed_text(query)
        )

        results = (
            self.vector_store
            .search(
                query_vector,
                limit=top_k
            )
        )

        return results