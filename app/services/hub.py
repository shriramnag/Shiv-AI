# श्री राम नाग जी, यह शिव एआई का फाइनल हब है जो आपके विज़न के सभी ८ स्टेप्स को जोड़ता है।
# इसमें सर्च, सोशल मीडिया, कोडिंग, और हकलाने का इलाज सब शामिल है।

from app.services.agent_service import agent_manager
from app.services.search_engine import search_port
from app.services.terminal_service import terminal_port
from app.services.vision_service import vision_manager
from app.services.voice_service import voice_engine
from app.services.media_agent import media_port # यूट्यूब और सोशल मीडिया के लिए
from app.services.groq_service import get_shiv_response # मुख्य दिमाग
from app.services.learning_engine import learner # खुद सीखने के लिए
from app.utils.response_formatter import clean_shiv_response # बिना हकलाए बोलने के लिए

class ShivAIHub:
    def __init__(self):
        # सभी स्पेशलिस्ट पोर्ट्स (Child Bots) को यहाँ रजिस्टर किया गया है
        self.ports = {
            "coding": agent_manager,
            "search": search_port,
            "system": terminal_port,
            "vision": vision_manager,
            "voice": voice_engine,
            "media": media_port
        }

    def process_command(self, user_input):
        """यह मुख्य फंक्शन है जो तय करेगा कि मालिक के आदेश पर क्या करना है"""
        cmd = user_input.lower()
        raw_response = ""

        # १. कोडिंग और बग फिक्सिंग (Coding Task Execution)
        if any(x in cmd for x in ["code", "bug", "सुधार", "fix"]):
            raw_response = self.ports["coding"].execute_task(user_input)
            learner.learn_new_info("Coding Agent", "नया कोडिंग टास्क पूरा किया")

        # २. यूट्यूब, फेसबुक और सोशल मीडिया रिसर्च
        elif any(x in cmd for x in ["youtube", "facebook", "यूट्यूब", "सोशल"]):
            raw_response = self.ports["media"].fetch_youtube_data(user_input)
            learner.learn_new_info("Media Port", raw_response)

        # ३. गूगल और विकिपीडिया (Online Research)
        elif any(x in cmd for x in ["google", "खोजो", "search", "wikipedia"]):
            raw_response = self.ports["search"].google_search(user_input)
            # रिसर्च से मिली जानकारी को अपनी याददाश्त में जोड़ना
            learner.learn_new_info("Internet Search", raw_response)

        # ४. विज़न और इमेज रिकॉग्निशन (Vision-based layer)
        elif any(x in cmd for x in ["देखो", "see", "camera", "image"]):
            raw_response = self.ports["vision"].analyze_visuals(user_input)

        # ५. सामान्य बातचीत और थिंकिंग (Core Brain)
        else:
            raw_response = get_shiv_response(user_input)

        # ६. फाइनल स्टेप: जवाब को 'हकलाने' से बचाना (Speech-to-Text Accuracy)
        # यहाँ हम नंबरों को शब्दों में बदल रहे हैं
        final_speech_ready_text = clean_shiv_response(raw_response)
        
        return final_speech_ready_text

# हब को सक्रिय करें
shiv_hub = ShivAIHub()
