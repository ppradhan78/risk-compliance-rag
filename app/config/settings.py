import os

from dotenv import load_dotenv

load_dotenv()


class Settings:

    QDRANT_URL = os.getenv(
        "QDRANT_URL",
        "http://localhost:6333"
    )

    QDRANT_COLLECTION = os.getenv(
        "QDRANT_COLLECTION",
        "risk_compliance_documents"
    )

    EMBEDDING_MODEL = os.getenv(
        "EMBEDDING_MODEL",
        "all-MiniLM-L6-v2"
    )

    TOP_K = int(
        os.getenv("TOP_K", "5")
    )


settings = Settings()