from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from datetime import datetime, UTC
from uuid import uuid4
from typing import Optional, List

# App initialization
app = FastAPI(
    title="SmartTalk Agent API",
    description="An interactive chatbot backend using FastAPI for intelligent conversations",
    version="1.0.0",
)


# Data Models 

# Meta info for each message session
class ChatContext(BaseModel):
    created_at: datetime = Field(default_factory=lambda: datetime.now(tz=UTC))
    conversation_id: str = Field(default_factory=lambda: str(uuid4()))

# Incoming message format
class ClientPrompt(BaseModel):
    sender_id: str
    message_text: str
    context: ChatContext
    keywords: Optional[List[str]] = None

# Response format
class BotReply(BaseModel):
    sender_id: str
    reply_text: str
    context: ChatContext


# Endpoints

# Root check
@app.get("/")
async def home():
    return {
        "info": "SmartTalk Agent API is up and running!",
        "docs": "/docs for Swagger UI"
    }

# Sample user info endpoint
@app.get("/profile/{sender_id}")
async def fetch_user_profile(sender_id: str, user_type: Optional[str] = None):
    return {
        "id": sender_id,
        "type": user_type or "anonymous"
    }

# Main chat POST endpoint
@app.post("/talk/", response_model=BotReply)
async def interact(prompt: ClientPrompt):
    if not prompt.message_text.strip():
        raise HTTPException(status_code=422, detail="Empty message received.")
    
    # Simulated reply logic
    smart_response = (
        f"Hi {prompt.sender_id}, I received your message: '{prompt.message_text}'. "
        "What would you like to talk about next?"
    )

    return BotReply(
        sender_id=prompt.sender_id,
        reply_text=smart_response,
        context=ChatContext()
    )
