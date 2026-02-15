# Import vector store loader to access stored embeddings
# This function is used to load the already-created vector database (ChromaDB)
from app.core.vector_store import get_vectorstore

# Import embedding model to embed user queries
# This is intended to be used for converting user queries into vectors
# (Note: imported here for RAG completeness, even if not directly used below)
from app.core.embeddings import embedding_model

# Import Groq LLM wrapper
# This function is responsible for generating text responses using Groq LLM
from app.core.llm import generate_text


def run_rag_pipeline(user_query: str):
    """
    This function executes the complete RAG pipeline.

    RAG pipeline stages:
    1. Accept user query
    2. Retrieve relevant document chunks from vector database
    3. Construct a context-aware prompt
    4. Generate final answer using Groq LLM
    """

    # Load the existing vector database (ChromaDB)
    # This vectorstore already contains embedded document chunks
    vectorstore = get_vectorstore()

    # Safety check to ensure vector database exists and is not empty
    # This prevents errors when querying before ingestion
    if vectorstore is None:
        return "Vector database is empty. Please ingest documents first."

    # Perform similarity search in the vector database
    # This retrieves the top-k most relevant chunks based on semantic similarity
    retrieved_docs = vectorstore.similarity_search(
        user_query,  # The user’s question used as the search query
        k=4          # Number of most relevant document chunks to retrieve
    )

    # Combine the content of all retrieved documents into a single context string
    # This context will be passed to the LLM for grounded answering
    context = "\n\n".join(doc.page_content for doc in retrieved_docs)

    # Construct the final prompt sent to the LLM
    # The prompt enforces strict grounding using retrieved context only
    prompt = f"""
You are an intelligent assistant.
Answer the question ONLY using the context below.
If the answer is not in the context, say "I don't know".

Context:
{context}

Question:
{user_query}

Answer:
"""

    # Call Groq LLM to generate a response based on the constructed prompt
    # This line is intended to invoke the LLM for text generation
    response = generate_text(prompt)

    # Return the final generated answer back to the API or caller
    return response