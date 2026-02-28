# श्री राम नाग जी, यह शिव एआई का मुख्य हब (Hub) है जो सभी चाइल्ड पोर्ट्स को जोड़ता है।
from app.services.agent_service import agent_manager
from app.services.search_engine import search_port
from app.services.terminal_service import terminal_port
from app.services.vision_service import vision_manager
from app.services.voice_service import voice_engine
from app.services.groq_service import get_shiv_response

class ShivAIHub:
    def __init__(self):
        # सभी स्पेशलिस्ट पोर्ट्स की पहचान
        self.ports = {
            "coding_port": agent_manager,
            "search_port": search_port,
            "system_port": terminal_port,
            "vision_port": vision_manager,
            "voice_port": voice_engine
        }

    def process_command(self, user_input):
        # यह लॉजिक तय करेगा कि कौन सा पोर्ट काम पर लगेगा
        cmd = user_input.lower()
        
        # १. कोडिंग और बग फिक्सिंग के लिए
        if "code" in cmd or "bug" in cmd or "सुधार" in cmd:
            return self.ports["coding_port"].execute_task(user_input)
            
        # २. इंटरनेट, गूगल या विकिपीडिया के लिए
        elif any(x in cmd for x in ["google", "खोजो", "search", "wikipedia"]):
            return self.ports["search_port"].google_search(user_input)
            
        # ३. सिस्टम कमांड या फाइल बनाने के लिए
        elif "terminal" in cmd or "folder" in cmd or "run" in cmd:
            return self.ports["system_port"].execute_command(user_input)
            
        # ४. अगर कुछ समझ न आए तो मुख्य दिमाग (Groq) से पूछो
        else:
            return get_shiv_response(user_input)

# हब को सक्रिय करना
shiv_hub = ShivAIHub()

