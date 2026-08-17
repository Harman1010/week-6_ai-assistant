from fastapi import FastAPI

from backend.routes.chat import router as chat_router


app = FastAPI(
    title="AI Assistant",
    description="Production-ready GenAI assistant with chat, RAG, memory, and tool calling.",
    version="1.0.0",
)


app.include_router(chat_router)


@app.get("/")
def root():
    return {
        "message": "AI Assistant API"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }