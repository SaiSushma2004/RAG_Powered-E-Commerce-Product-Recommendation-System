# app/core/document_loader.py
# This file is responsible for loading documents from disk
# It supports multiple file types (PDF and TXT) and converts them into LangChain documents

# Import document loaders from LangChain Community
# PyPDFLoader is used to read PDF files
# TextLoader is used to read plain text (.txt) files
from langchain_community.document_loaders import PyPDFLoader, TextLoader

# Import os module to work with file paths and extensions
import os

def load_documents(file_path: str):
    """
    This function:
    - Takes a file path as input
    - Detects the file type (PDF or TXT)
    - Uses the appropriate loader
    - Returns loaded documents in LangChain format
    """

    # Extract the file extension from the given file path
    # Example: ".pdf" or ".txt"
    extension = os.path.splitext(file_path)[1].lower()

    # Check if the file is a PDF
    if extension == ".pdf":
        # Initialize the PDF loader with the given file path
        loader = PyPDFLoader(file_path)

    # Check if the file is a text file
    elif extension == ".txt":
        # Initialize the text loader with UTF-8 encoding
        # UTF-8 ensures special characters are handled correctly
        loader = TextLoader(file_path, encoding="utf-8")

    # If the file type is neither PDF nor TXT
    else:
        # Raise an error to prevent unsupported file types
        raise ValueError(f"Unsupported file type: {extension}")

    # Load the document content using the selected loader
    # This converts the file into a list of LangChain Document objects
    documents = loader.load()

    # Return the loaded documents to be used for chunking and embedding
    return documents