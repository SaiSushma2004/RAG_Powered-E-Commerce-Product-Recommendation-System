# upload.py
# REST API for dynamic document ingestion
# This file allows users to upload documents dynamically via an API endpoint

# Import os module (used for file path handling if needed later)
import os

# Import APIRouter to create API routes
# Import UploadFile and File to handle file uploads in FastAPI
from fastapi import APIRouter, UploadFile, File

# Import document loading logic that reads and splits documents into chunks
from app.core.document_loader import load_documents

# Import vector store logic to store embeddings in ChromaDB
from app.core.vector_store import get_vectorstore

# Create an APIRouter instance for grouping upload-related routes
router = APIRouter()

# Define a POST API endpoint at /upload
# This endpoint accepts a file uploaded by the user
@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    """
    This function:
    - Accepts a file uploaded by the user
    - Saves the file locally
    - Splits the document into chunks
    - Generates embeddings
    - Stores them in ChromaDB
    """

    # Define the path where the uploaded file will be saved
    # The file is stored inside app/data/documents/
    save_path = f"app/data/documents/{file.filename}"

    # Open the destination file in binary write mode
    # This ensures any type of file (PDF, TXT, etc.) can be saved
    with open(save_path, "wb") as f:
        # Read the uploaded file asynchronously and write it to disk
        f.write(await file.read())

    # Load and split the uploaded document into chunks
    # This prepares the document for embedding and retrieval
    documents = load_documents(save_path)

    # Get the ChromaDB vector store instance
    vectorstore = get_vectorstore()

    # Add the document chunks to the vector database
    vectorstore.add_documents(documents)

    # Persist the embeddings so they are saved permanently
    vectorstore.persist()

    # Return a success response with the number of chunks stored
    return {
        "message": "File uploaded and indexed successfully",
        "chunks": len(documents)
    }