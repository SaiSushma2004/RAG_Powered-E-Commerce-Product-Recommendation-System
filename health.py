"""
Health check endpoint
Used to verify whether the API service is running and reachable
"""

# Import APIRouter from FastAPI to define API routes
from fastapi import APIRouter

# Create an APIRouter instance
# prefix="/health" means all routes in this file will start with /health
router = APIRouter(prefix="/health")

# Define a GET API endpoint at /health
@router.get("")
def health_check():
    """
    This function is used to:
    - Confirm that the backend API is up and running
    - Provide a simple response for monitoring tools or manual testing
    """

    # Return a JSON response indicating service status
    return {
        "status": "ok",              # Indicates the API is healthy
        "service": "RAG Q&A API"     # Identifies the running service
    }