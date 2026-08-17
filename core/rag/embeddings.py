from langchain_huggingface import HuggingFaceEmbeddings

from core.config import settings


def get_embeddings():

    return HuggingFaceEmbeddings(
        model_name=settings.embedding_model,
        model_kwargs={
            "device": "cpu"
        },
        encode_kwargs={
            "normalize_embeddings": True
        },
    )