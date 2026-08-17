from pathlib import Path
from uuid import uuid4

from fastapi import APIRouter, File, HTTPException, UploadFile

from core.rag.loader import load_document
from core.rag.splitter import split_documents
from core.rag.vectorstore import get_vectorstore


router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):

    extension = Path(file.filename or "").suffix.lower()

    if extension not in {".pdf", ".txt", ".md"}:
        raise HTTPException(
            status_code=400,
            detail="Only PDF, TXT and MD files are supported."
        )

    content = await file.read()

    upload_dir = Path("data/uploads")
    upload_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    filename = f"{uuid4().hex}{extension}"
    file_path = upload_dir / filename

    file_path.write_bytes(content)

    try:

        documents = load_document(
            str(file_path)
        )

     
        chunks = split_documents(
            documents
        )

       
        vectorstore = get_vectorstore()

        vectorstore.add_documents(
            chunks
        )

    except Exception as exc:
        file_path.unlink(
            missing_ok=True
        )

        raise HTTPException(
            status_code=500,
            detail=f"Document processing failed: {exc}"
        )

    return {
        "filename": file.filename,
        "chunks": len(chunks),
        "message": "Document uploaded and indexed successfully."
    }