from fastapi import APIRouter

from backend.schemas.chat import ChatRequest,ChatResponse,Source

from core.llm.service import LLMService
from core.rag.retriever import retrieve_documents
from core.memory.service import MemoryService


router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)

llm_service = LLMService()
memory_service = MemoryService()


@router.post("/", response_model=ChatResponse)
def chat(request: ChatRequest):

    history = memory_service.get_history(request.session_id)

    results = retrieve_documents(
        request.question
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
        message=request.question,
        context=context,
        history=history
    )

    memory_service.add_message(
        request.session_id,
        "user",
        request.question
    )

    memory_service.add_message(
        request.session_id,
        "assistant",
        response
    )

    return ChatResponse(
        answer=response,
        sources=sources,
    )