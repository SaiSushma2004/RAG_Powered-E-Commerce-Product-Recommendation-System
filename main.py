"""
Main entry point of FastAPI application

Purpose:
- This file initializes the FastAPI server
- Registers all API routes (health, query, upload)
- Acts as the application startup file
"""

# Import FastAPI class
# FastAPI is the web framework used to build REST APIs
from fastapi import FastAPI

# Import the health check router
# This router is responsible for checking whether the API is running
from app.api.health import router as health_router

# Import the query router
# This router handles user questions and performs RAG-based answering
from app.api.query import router as query_router

# Import the upload router
# This router allows users to dynamically upload documents for ingestion
from app.api.upload import router as upload_router

# Create the FastAPI application instance
# The title is shown in Swagger UI and API documentation
app = FastAPI(
    title="E-Commerce Product Recommendation using RAG"
)

# Register the health router with the FastAPI app
# Enables the /health endpoint
app.include_router(health_router)

# Register the query router with the FastAPI app
# Enables the /query endpoint for asking questions
app.include_router(query_router)

# Register the upload router with the FastAPI app
# Enables the /upload endpoint for dynamic document ingestion
app.include_router(upload_router)