# This project is an AI Assistant that collects well-experimented chunks from the documents and generates natural language answer for user query combined with source citation , conversation memory and isloated environment validation

---

## Features

- RAG-based document question answering
- Experimented document chunking strategy
- Semantic search using Chroma
- Source citation with retrieved document metadata
- Support for PDF, TXT, and Markdown documents
- SHA-256 based duplicate document detection
- Session-based conversation memory
- FastAPI backend
- Gradio frontend
- Docker-based isolated environment

---

### Chunking Experiment

Different chunking configurations were evaluated using a fixed set of RAG questions.

| Chunk Size | Overlap | Evaluation |
|---:|---:|---|
| 600 | 120 | Good retrieval; partial end-to-end validation |
| **800** | **120** | **Selected baseline** |
| 1000 | 120 | Good retrieval and end-to-end answers |

The final configuration selected for the current project is:

```text
chunk_size = 800
chunk_overlap = 120
```

## Project Structure

```text
AI-Assistant/
│
├── backend/
│   ├── routes/
│   │   ├── chat.py
│   │   └── ingestion.py
│   │
│   ├── schemas/
│   │   └── ...
│   │
│   └── main.py
│
├── core/
│   ├── rag/
│   │   ├── embeddings.py
│   │   ├── splitter.py
│   │   ├── vectorstore.py
│   │   └── ...
│   │
│   └── config.py
│
├── data/
│   ├── uploads/
│   │   └── ...
│   │
│   └── vectorstore/
│       └── ...
│
├── tests/
│   ├── rag_test_cases.py
│   ├── test_rag.py
│   └── test_retrieval.py
│
├── test_results.md
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

### Structure Overview

- `backend/` — FastAPI application layer containing API routes and request/response schemas.
- `core/rag/` — Core RAG pipeline including document chunking, embeddings, retrieval, and Chroma integration.
- `core/config.py` — Central configuration including chunk size, overlap, model settings, and environment configuration.
- `data/uploads/` — Stores uploaded source documents.
- `data/vectorstore/` — Persistent Chroma vector database containing embedded document chunks.
- `tests/rag_test_cases.py` — Fixed evaluation questions used across RAG experiments.
- `tests/test_rag.py` — End-to-end test runner that sends questions through the FastAPI chat endpoint.
- `tests/test_retrieval.py` — Retrieval-only testing for evaluating chunking configurations without invoking the LLM.
- `test_results.md` — Records results from the chunking and RAG experiments.

---

## Tech Stack

### Backend

- FastAPI
- Schema validation
- Routes

### Core

- LangChain
- RAG
- Chroma

---

## Setup Guide

1. Clone the repository

```powershell

git clone <repository-url>
cd AI-Assistant

```

2. Create a virtual environment

```powershell

python -m venv venv

```

3. Activate virtual environment

```powershell 

venv/Scripts/Activate.ps1

```

4. Create .env file (Refer to .env.example)

```powershell

GEMINI_API_KEY=your_api_key

```

5. Start the FastAPI Backend

```powershell

uvicorn backend.main:app

```

6. Start the frontend

```powershell

python -m frontend.app

```
---

## Limitations

- Retrieval strategy is currently limited to semantic search.
- Agentic RAG is not supported.
- Conversation memory is currently session-based and in-memory.
- No persistent user authentication or user-specific document isolation.
- Retrieval evaluation is currently primarily qualitative rather than based on formal retrieval metrics.

---


## Future Improvements

- Hybrid search combining semantic and keyword retrieval
- Reranking retrieved documents
- Formal retrieval evaluation metrics
- Latency and cost optimization
- Response caching
- LLM gateways
- Persistent conversation storage
- User authentication and document-level access control
- Agentic RAG
- Production-ready deployment and monitoring