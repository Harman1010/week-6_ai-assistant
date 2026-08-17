# This project is an AI Assistant that collects well-experimented chunks from the documents and generates natural language answer for user query combined with source citation , conversation memory and isloated environment validation

---

## Features

- Chunks well experimented
- Conversation memory support
- Containerization using Docker

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







---




## Limitations

- Retrieval strategy is only semantic search
- Agentic RAG is not supported


## Future Improvements

- Add Latency , Cost Optimization
- Support Cache
- LLM Gateways