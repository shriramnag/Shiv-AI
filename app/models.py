from pydantic import BaseModel

class ChatRequest(BaseModel):
    message: str
    user_id: str = "default_user"

class ChatResponse(BaseModel):
    shiv_ai_says: str
    owner: str = "Shri Ram nag"
  
