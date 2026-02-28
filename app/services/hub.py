# श्री राम नाग जी, यह शिव एआई का मास्टर हब है।
# यह कोडिंग, सर्च, लर्निंग और वॉइस को एक साथ जोड़ता है।

from app.services.agent_service import agent_manager
from app.services.search_engine import search_port
from app.services.terminal_service import terminal_port
from app.services.vision_service import vision_manager
from app.services.voice_service import voice_engine
from app.services.media_agent import media_port
from app.services.groq_service import get_shiv_response
from app.services.learning_engine import learner # सीखने वाला लॉजिक
from app.utils.response_formatter import clean_shiv_response # हकलाने का इलाज

class ShivAIHub:
    def __init__(self):
        # सभी स्पेशलिस्ट चाइल्ड पोर्ट्स का कनेक्शन
        self.ports = {
            "coding": agent_manager,
            "search": search_port,
            "terminal": terminal_port,
            "vision": vision_manager,
            "voice": voice_engine,
            "media": media_port
        }

    def process_command(self, user_input):
        cmd = user_input.lower()
        response_text = ""

        # १. कोडिंग, बग फिक्सिंग और फाइल स्ट्रक्चर के लिए
        if any(x in cmd for x in ["code", "bug", "सुधार", "कोडिंग", "fix"]):
            response_text = self.ports["coding"].execute_task(user_input)
            # कोडिंग के नए तरीके सीखना
            learner.learn_new_info("Coding Agent", f"मालिक के लिए कोड टास्क पूरा किया: {user_input}")

        # २. यूट्यूब और सोशल मीडिया के लिए
        elif any(x in cmd for x in ["youtube", "facebook", "social", "यूट्यूब"]):
            response_text = self.ports["media"].fetch_youtube_data(user_input)
            learner.learn_new_info("Social Media Port", response_text)

        # ३. गूगल, विकिपीडिया और ऑनलाइन रिसर्च के लिए
        elif any(x in cmd for x in ["google", "search", "खोजो", "wikipedia"]):
            response_text = self.ports["search"].google_search(user_input)
            # ऑनलाइन मिली जानकारी से खुद को ट्रेन करना
            learner.learn_new_info("Online Research", response_text)

        # ४. सिस्टम कमांड और टर्मिनल कंट्रोल के लिए
        elif "run" in cmd or "terminal" in cmd or "command" in cmd:
            response_text = self.ports["terminal"].execute_command(user_input)

        # ५. सामान्य बातचीत के लिए मुख्य दिमाग (Groq) का उपयोग
        else:
            response_text = get_shiv_response(user_input)
            # बातचीत से यूजर की पसंद सीखना
            learner.learn_new_info("User Chat", f"मालिक की बात: {user_input}")

        # ६. फाइनल स्टेप: जवाब को साफ़ करना (नंबरों को शब्दों में बदलना)
        # ताकि शिव एआई बिना हकलाए साफ़ शब्दों में बोले।
        final_output = clean_shiv_response(response_text)
        
        return final_output

# हब को सक्रिय (Activate) करना
shiv_hub = ShivAIHub()
