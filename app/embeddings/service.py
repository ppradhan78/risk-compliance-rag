from sentence_transformers import SentenceTransformer

from app.config.settings import settings


class EmbeddingService:

    def __init__(self):

        self.model = SentenceTransformer(
            settings.EMBEDDING_MODEL
        )

    def embed_text(
        self,
        text: str
    ) -> list[float]:

        vector = self.model.encode(
            text
        )

        return vector.tolist()

    def embed_documents(
        self,
        texts: list[str]
    ) -> list[list[float]]:

        vectors = self.model.encode(
            texts
        )

        return vectors.tolist()