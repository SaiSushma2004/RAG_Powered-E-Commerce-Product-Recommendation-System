"""
Pydantic models for request validation

Purpose:
- This file defines data schemas used to validate incoming API requests
- Ensures the request body follows a fixed structure before processing
"""

# Import BaseModel from Pydantic
# Pydantic is used by FastAPI to validate and parse request data
from pydantic import BaseModel

# Define a request model for question-based APIs (e.g., /query)
# This ensures that the incoming request body must contain a "question" field
class QuestionRequest(BaseModel):

    # The user's question as a string
    # FastAPI automatically validates that this field exists and is of type str
    question: str