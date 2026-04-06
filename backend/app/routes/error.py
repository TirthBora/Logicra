from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class ErrorRequest(BaseModel):
    error_message: str
    language: str

class ErrorResponse(BaseModel):
    explanation: str
    fix_suggestion: str

@router.post("/", response_model=ErrorResponse)
async def translate_error(request: ErrorRequest):
    # TODO: Error translation
    return ErrorResponse(explanation="TODO", fix_suggestion="TODO")

