from groq import Groq
from config import GROQ_API_KEY, MODEL_NAME, OWNER_NAME, AI_NAME

client = Groq(api_key=GROQ_API_KEY)

def get_ai_response(user_query, system_context):
    # एआई को निर्देश कि वह नंबरों को शब्दों में लिखे
    prompt_enhancement = "\nयाद रहे: सभी नंबरों को हिंदी शब्दों में लिखो और डॉट (.) की जगह कोमा (,) लगाओ।"
    
    completion = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": system_context + prompt_enhancement},
            {"role": "user", "content": user_query}
        ]
    )
    return completion.choices[0].message.content
  
