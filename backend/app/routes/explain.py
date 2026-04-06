from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class ExplainRequest(BaseModel):
    code: str
    language: str

class ExplainResponse(BaseModel):
    explanation: str

@router.post("/", response_model=ExplainResponse)
async def explain_code(request: ExplainRequest):
    # TODO: AI explanation
    return ExplainResponse(explanation="TODO: AI-powered explanation")

