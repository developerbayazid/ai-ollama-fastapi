from fastapi import APIRouter
from services.ai_service import generate_response

router = APIRouter()

@router.post("/chat")
async def chat(message: str):
    return generate_response(message)
    