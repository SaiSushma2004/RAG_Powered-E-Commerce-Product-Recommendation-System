# query.py
# This file is responsible for handling question-answering requests using the RAG pipeline

# Import APIRouter from FastAPI to create API routes/endpoints
from fastapi import APIRouter

# Import BaseModel from Pydantic to define request body schema
from pydantic import BaseModel

# Import the function that returns the vector database (ChromaDB)
from app.core.vector_store import get_vectorstore

# Import the function that generates text using the LLM
from app.core.llm import generate_text

# Create an APIRouter instance to register API endpoints
router = APIRouter()

# Define the expected request body structure for the /query API
class QueryRequest(BaseModel):
    # The question field represents the user’s query/question
    question: str

# Define a POST API endpoint at /query
@router.post("/query")
def query_documents(request: QueryRequest):
    """
    This function:
    1. Accepts a question from the user
    2. Retrieves relevant documents from the vector database
    3. Builds a context-aware prompt
    4. Generates an answer using the LLM
    """

    # Get the vector store instance (ChromaDB) that contains document embeddings
    vectorstore = get_vectorstore()

    # Perform similarity search in the vector database using the user question
    # k=3 means retrieve the top 3 most relevant document chunks
    docs = vectorstore.similarity_search(request.question, k=3)

    # Combine the content of retrieved documents into a single context string
    # Each document’s page_content is joined with double newlines
    context = "\n\n".join(doc.page_content for doc in docs)
    
    # Create the prompt for the LLM
    # The prompt explicitly instructs the LLM to answer ONLY using the provided context
    prompt = f"""
    Answer strictly based on the context below.

    Context:
    {context}

    Question:
    {request.question}
    """

    # Pass the constructed prompt to the LLM to generate an answer
    answer = generate_text(prompt)

    # Return the generated answer as a JSON response
    return {"answer": answer}
