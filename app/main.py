from fastapi import FastAPI
from app.services.groq_service import get_ai_response
from config import AI_NAME, OWNER_NAME

app = FastAPI(title=f"{AI_NAME} API")

# सिस्टम कॉन्टेक्स्ट लोड करना
with open("database/learning_data/system_context.txt", "r", encoding="utf-8") as f:
    system_logic = f.read()

@app.get("/")
def home():
    return {"status": "Online", "owner": OWNER_NAME, "bot_name": AI_NAME}

@app.post("/chat")
async def chat(message: str):
    # टर्बो स्पीड प्रोसेसिंग
    response = get_ai_response(message, system_logic)
    return {"shiv_ai_says": response}
  
