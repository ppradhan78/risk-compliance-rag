from app.retrieval.retriever import Retriever


class RAGService:

    def __init__(self):

        self.retriever = Retriever()

    def retrieve_context(
        self,
        question: str,
        top_k: int = 5
    ):

        results = (
            self.retriever
            .retrieve(
                question,
                top_k
            )
        )

        contexts = []

        for result in results:

            contexts.append({
                "text": result.payload["text"],
                "document":
                    result.payload.get(
                        "document_name"
                    ),
                "page":
                    result.payload.get(
                        "page_number"
                    ),
                "document_type":
                    result.payload.get(
                        "document_type"
                    )
            })

        return contexts