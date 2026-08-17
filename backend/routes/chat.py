from fastapi import APIRouter

from backend.schemas.chat import ChatRequest,ChatResponse,Source

from core.llm.service import LLMService
from core.rag.retriever import retrieve_documents


router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)

llm_service = LLMService()


@router.post("/", response_model=ChatResponse)
def chat(request: ChatRequest):

    results = retrieve_documents(
        request.message
    )

    context_parts = []
    sources = []

    for document, score in results:

        context_parts.append(
            document.page_content
        )

        sources.append(
            Source(
                document=document.metadata.get(
                    "source",
                    "unknown"
                ),
                page=document.metadata.get(
                    "page"
                ),
                score=float(score),
            )
        )

    context = "\n\n---\n\n".join(
        context_parts
    )

    response = llm_service.generate(
        message=request.message,
        context=context,
    )

    return ChatResponse(
        response=response,
        sources=sources,
    )