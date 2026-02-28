# श्री राम नाग जी, यह शिव एआई का फाइनल हब है जो सभी पोर्ट्स को जोड़ता है।
from app.services.agent_service import agent_manager
from app.services.search_engine import search_port
from app.services.terminal_service import terminal_port
from app.services.vision_service import vision_manager
from app.services.voice_service import voice_engine
from app.services.media_agent import media_port # <-- नया जोड़ा गया
from app.services.groq_service import get_shiv_response
from app.utils.response_formatter import clean_shiv_response # <-- हकलाने का इलाज

class ShivAIHub:
    def __init__(self):
        # सभी स्पेशलिस्ट पोर्ट्स की लिस्ट
        self.ports = {
            "coding_port": agent_manager,
            "search_port": search_port,
            "system_port": terminal_port,
            "vision_port": vision_manager,
            "voice_port": voice_engine,
            "media_port": media_port
        }

    def process_command(self, user_input):
        cmd = user_input.lower()
        
        # १. कोडिंग और बग फिक्सिंग
        if any(x in cmd for x in ["code", "bug", "सुधार", "कोडिंग"]):
            raw_response = self.ports["coding_port"].execute_task(user_input)
            
        # २. यूट्यूब, फेसबुक और सोशल मीडिया
        elif any(x in cmd for x in ["youtube", "facebook", "यूट्यूब", "सोशल"]):
            raw_response = self.ports["media_port"].fetch_youtube_data(user_input)
            
        # ३. गूगल और विकिपीडिया सर्च
        elif any(x in cmd for x in ["google", "खोजो", "search", "wikipedia"]):
            raw_response = self.ports["search_port"].google_search(user_input)
            
        # ४. अगर कुछ समझ न आए तो मुख्य दिमाग (Groq)
        else:
            raw_response = get_shiv_response(user_input)

        # ५. जवाब को साफ़ करना (नंबरों को शब्दों में बदलना)
        # ताकि शिव एआई बिना हकलाए बोल सके
        final_speech = clean_shiv_response(raw_response)
        return final_speech

# हब को सक्रिय करना
shiv_hub = ShivAIHub()
