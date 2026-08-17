from pathlib import Path

from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
)


def load_document(file_path: str):

    """Loads document using Langchain loaders"""

    path = Path(file_path)

    if path.suffix.lower() == ".pdf":
        loader = PyPDFLoader(str(path))

    elif path.suffix.lower() in {".txt", ".md"}:
        loader = TextLoader(
            str(path),
            encoding="utf-8"
        )

    else:
        raise ValueError(
            "Only PDF, TXT and MD files are supported."
        )

    return loader.load()