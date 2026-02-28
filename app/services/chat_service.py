from app.services.groq_service import get_shiv_response
from app.services.vector_store import vector_db
from config import OWNER_NAME

def process_user_chat(user_id, user_message):
    # १. पहले याददाश्त में चेक करो (Search Context)
    past_context = vector_db.search_context(user_message)
    
    # २. दिमाग (LLM) से जवाब मांगो
    full_prompt = f"पुरानी यादें: {past_context}\nअभी की बात: {user_message}"
    response = get_shiv_response(full_prompt)
    
    # ३. नई बात को याददाश्त में सुरक्षित करो
    vector_db.add_information(f"मालिक ने कहा: {user_message}. मैंने कहा: {response}")
    
    return response
  
