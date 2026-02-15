# embeddings.py
# This file is responsible for converting text into numerical vectors (embeddings)
# Embeddings are required for similarity search in the vector database (ChromaDB)

# Import HuggingFaceEmbeddings from LangChain
# This class allows us to use Hugging Face sentence-transformer models
from langchain_huggingface import HuggingFaceEmbeddings

def get_embedding_function():
    """
    This function:
    - Initializes an embedding model
    - Converts text chunks into numerical vectors
    - These vectors are later stored in ChromaDB for similarity search
    """

    # Return an instance of HuggingFaceEmbeddings
    # The model 'all-MiniLM-L6-v2' is:
    # - Lightweight
    # - Fast
    # - Free
    # - Commonly used for RAG pipelines
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )