# vectorstore.py
# This file is responsible for handling all vector database operations
# It uses ChromaDB ONLY for storing and retrieving embeddings

# Import Chroma vector store implementation from LangChain community package
# Chroma is used to persist embeddings locally on disk
from langchain_community.vectorstores import Chroma

# Import the embedding function
# This function converts text into numerical vectors
from app.core.embeddings import get_embedding_function

# Define the directory path where ChromaDB data will be stored
# This folder will contain all vector embeddings and metadata
CHROMA_PATH = "app/data/chroma"

def get_vectorstore():
    """
    Loads an existing ChromaDB instance or creates a new one if it doesn't exist.

    Purpose:
    - Ensures a single, consistent vector database is used across the application
    - Allows reuse of previously ingested document embeddings
    """

    # Initialize and return a Chroma vector store instance
    # persist_directory tells Chroma where to store/load vectors on disk
    # embedding_function specifies how text is converted into embeddings
    return Chroma(
        persist_directory=CHROMA_PATH,
        embedding_function=get_embedding_function()
    )