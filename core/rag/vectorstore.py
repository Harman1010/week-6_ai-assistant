from langchain_chroma import Chroma

from core.config import settings
from core.rag.embeddings import get_embeddings


def get_vectorstore():

    return Chroma(
        collection_name="dstarix_documents",
        embedding_function=get_embeddings(),
        persist_directory="./data/vectorstore",
    )