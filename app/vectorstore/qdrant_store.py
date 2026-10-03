from qdrant_client import QdrantClient

from qdrant_client.models import (
    Distance,
    VectorParams,
    PointStruct
)

from app.config.settings import settings


class QdrantStore:

    def __init__(self):

        self.client = QdrantClient(
            url=settings.QDRANT_URL
        )

        self.collection_name = (
            settings.QDRANT_COLLECTION
        )

        self.create_collection()

    def create_collection(self):

        collections = (
            self.client
            .get_collections()
            .collections
        )

        exists = any(
            c.name == self.collection_name
            for c in collections
        )

        if not exists:

            self.client.create_collection(
                collection_name=self.collection_name,
                vectors_config=VectorParams(
                    size=384,
                    distance=Distance.COSINE
                )
            )

    def upsert(
        self,
        points: list[PointStruct]
    ):

        self.client.upsert(
            collection_name=self.collection_name,
            points=points
        )

    def search(
        self,
        vector: list[float],
        limit: int = 5
    ):

        return self.client.query_points(
            collection_name=self.collection_name,
            query=vector,
            limit=limit
        ).points