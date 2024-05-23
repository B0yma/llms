from fastapi import APIRouter
from api.endpoints.v1 import gemini_conversation, gemini_conversation_delete, groq_conversation

api_router = APIRouter()

api_router.include_router(gemini_conversation.router, prefix="/api/v1/gemini/conversations", tags=["/api/v1/gemini/conversations"])

api_router.include_router(gemini_conversation_delete.router, prefix="/api/v1/gemini/conversations/delete", tags=["/api/v1/gemini/conversations/delete"])

api_router.include_router(groq_conversation.router, prefix="/api/v1/groq/conversations", tags=["/api/v1/groq/conversations"])