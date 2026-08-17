from core.config import settings
from core.rag.vectorstore import get_vectorstore


def retrieve_documents(query: str):
    vectorstore = get_vectorstore()

    results = vectorstore.similarity_search_with_score(
        query,
        k=settings.top_k
    )

    return results