from pydantic import BaseModel
from typing import Optional, Text


class ChatRequest(BaseModel):
    message_id: Optional[str] = None
    userPromptUrlEncoded: Optional[str] = None
    systemPromptUrlEncoded: Optional[str] = None
    llmModel: Optional[str] = None
    image: Optional[bool] = False
    image_url: Optional[str] = None


class ChatResponse(BaseModel):
    response: Text