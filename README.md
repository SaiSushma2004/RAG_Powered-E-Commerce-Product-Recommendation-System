# E-Commerce Product Recommendation System with RAG Pipeline

## Overview
This project implements an **E-Commerce Product Recommendation System** using a **Retrieval-Augmented Generation (RAG) pipeline**.  
It allows users to query product documents and get AI-generated responses based on both **statically uploaded files** and **dynamically uploaded files**.  

The project leverages:
- **ChromaDB** for embedding-based vector search
- **Grok LLM** for text generation
- **FastAPI** to expose REST API endpoints
- **LangChain** for document loading, chunking, and embeddings

This system ensures that product-related questions are answered intelligently using relevant document context.

---

## Project Features
1. **Static Document Ingestion**
   - Pre-defined files (e.g., `products.txt`) are ingested and indexed into ChromaDB.
   - Use `inject.py` for independent ingestion.

2. **Dynamic Document Upload**
   - Users can upload new product documents via API.
   - Uploaded documents are processed into embeddings and stored in ChromaDB.

3. **REST API Endpoints**
   - `GET /health` – Health check of API service
   - `POST /query` – Submit a question and get AI-generated answers using RAG
   - `POST /upload` – Upload files dynamically for ingestion

4. **RAG Pipeline**
   - Embeds user queries
   - Retrieves relevant chunks from ChromaDB
   - Generates answers using Grok LLM
   - Answers strictly based on document context

5. **Extensible**
   - Supports PDF and TXT files
   - Easy to swap LLM models or embedding backends

---

## Project Structure
project_root/ │ ├── app/ │   ├── api/ │   │   ├── health.py          # Health check API │   │   ├── query.py           # Question answering API │   │   └── upload.py          # Dynamic document ingestion API │   │ │   ├── core/ │   │   ├── document_loader.py # Handles PDF/TXT loading and chunking │   │   ├── embeddings.py      # Returns embedding model │   │   ├── llm.py             # Grok LLM wrapper for text generation │   │   ├── vectorstore.py     # ChromaDB integration │   │   └── rag_pipeline.py    # Executes complete RAG pipeline │   │ │   └── data/ │       └── documents/         # Folder for static and dynamic document storage │ ├── tests/ │   ├── test_env.py            # Tests .env and API key loading │   └── test_llm.py            # Tests Grok LLM text generation │ ├── inject.py                  # Static document ingestion script ├── app.py                     # FastAPI main application entrypoint ├── .env                       # Environment variables (API keys) ├── requirements.txt           # Python dependencies └── README.md                  # Project documentation


---

## Setup Instructions

### 1. Clone the repository

git clone <your-repo-link>
cd project_root

2. Install dependencies
pip install -r requirements.txt

requirements.txt
fastapi==0.101.1
uvicorn==0.23.2
python-dotenv==1.0.0
langchain==1.2.10
langchain-community==0.4.1
chromadb==0.4.5
huggingface-hub==0.18.1
sentence-transformers==2.2.2
groq==0.3.1
pydantic==1.10.12

4. Setup environment variables
Create a .env file in the project root:

GROQ_API_KEY=your_groq_api_key_here

4. Run static document ingestion
python inject.py
This indexes products.txt into ChromaDB.

5. Run FastAPI server
uvicorn app:app --reload

7. Test endpoints
Swagger UI: Open http://127.0.0.1:8000/docs�
Health check: GET /health
Query documents: POST /query with JSON { "question": "Your question here" }
Upload new document: POST /upload and choose file dynamically

9. Test LLM
python tests/test_llm.py
Ensures Grok LLM is working and generating responses correctly.

Design Decisions
ChromaDB for embeddings: lightweight, fast, easy to persist locally.
Grok LLM: selected for text generation (cloud-hosted, supports API tokens).
LangChain loaders: support for PDF and TXT ingestion.
Static + Dynamic ingestion: satisfies both developer and user upload scenarios.
RAG pipeline modularization: rag_pipeline.py separates query retrieval, embedding, and LLM generation logic.

How It Works
Static ingestion – Predefined files are converted into embeddings and stored in ChromaDB.
Dynamic ingestion – User uploads files via API; files are split, embedded, and stored.
Querying – User submits a question; RAG pipeline:
Embeds query
Retrieves top-k similar document chunks
Sends prompt to Grok LLM
Returns answer strictly based on retrieved context
API – FastAPI exposes endpoints for health check, query, and document upload.

Further Improvements

Support multiple LLM providers (OpenAI, HuggingFace) to increase reliability
Add authentication & user roles for secure API usage
Introduce PDF parsing enhancements for better chunking
Add vector store caching for faster repeated queries
Deploy on cloud platforms (Render, Railway, AWS) for production use
Expand multi-language support for documents
Add logging and error monitoring for better debugging

