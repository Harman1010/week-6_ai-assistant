from langchain_text_splitters import RecursiveCharacterTextSplitter

from core.config import settings


def split_documents(documents):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=settings.chunk_size,
        chunk_overlap=settings.chunk_overlap,
    )
    

    chunks = splitter.split_documents(documents)

     print(f"Number of chunks: {len(chunks)}")

    for i, chunk in enumerate(chunks):
            print(f"\n--- CHUNK {i} ---")
            print(f"Length: {len(chunk.page_content)}")
            print(chunk.page_content)

    return chunks