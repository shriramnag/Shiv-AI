# ****************************************************************************
# प्रोजेक्ट का नाम: शिव एआई (SHIV AI)
# मालिक: श्री राम नाग (Shri Ram nag)
# फाइल: hub.py (The Complete 27-Bot Master Controller)
# ****************************************************************************

import os
from app.utils.response_formatter import clean_shiv_response

# १. कोडिंग और टेक्निकल विभाग (Coding & Tech)
from app.services.agent_service import agent_manager      # कोडिंग मास्टर
from app.services.terminal_service import terminal_bot   # कमांड लाइन कंट्रोल
from app.services.learning_engine import self_learner    # खुद से सीखने वाला

# २. सुरक्षा और शातिर डिफेंस (Security & Ghost Defense)
from app.services.ghost_protocol_bot import ghost_bot      # चकमा देने वाला
from app.services.security_elite import elite_defense      # टाइम लॉक/मिरर
from app.services.network_sniper import sniper_bot        # वायरस हंटर
from app.services.cyber_security_agent import cyber_sec   # 24/7 मॉनिटरिंग
from app.services.defense_repair_bot import repair_bot    # सेल्फ-रिपेयर

# ३. मोबाइल और हार्डवेयर इंटीग्रेशन (Mobile & Hardware)
from app.services.system_integrator_bot import integrator_bot # यूनिवर्सल लिंक
from app.services.visual_hand_agent import hand_agent          # डिजिटल हाथ
from app.services.vision_service import vision_bot            # एआई की आँखें
from app.services.stt_service import ear_bot                 # सुनने की शक्ति
from app.services.voice_service import voice_bot             # बोलने की शक्ति

# ४. इंटरनेट और डिटेक्टिव विभाग (Web & OSINT Detective)
from app.services.web_navigator_bot import web_nav_bot     # अनलिमिटेड वेब
from app.services.osint_detective_bot import osint_bot     # लोकेशन/आईपी ट्रेस
from app.services.media_agent import social_bot           # यूट्यूब/सोशल मीडिया
from app.services.public_safety_bot import safety_bot      # जन-कल्याण सुरक्षा

# ५. कंटेंट और डिजाइन विभाग (Content & Stylist)
from app.services.content_creator_bot import content_bot   # राइटिंग/रिसर्च
from app.services.stylist_writer_bot import stylist_bot    # सजावट/फॉर्मेटिंग
from app.services.file_manager_bot import file_bot         # अपलोड/मैनेजमेंट

# ६. ज्ञान और विज्ञान विभाग (Knowledge & Ayurveda)
from app.services.ayurveda_bot import ayurveda_expert      # प्राचीन चिकित्सा
from app.services.mythology_bot import mythology_expert    # पुराण/महाभारत
from app.services.chat_service import memory_bot           # याददाश्त

class ShivAIHub:
    def __init__(self):
        # यहाँ आपके सभी २७+ बॉट्स की लिस्ट है (The Ultimate Army)
        self.army = {
            "coding": agent_manager, "terminal": terminal_bot, "learning": self_learner,
            "ghost": ghost_bot, "elite": elite_defense, "sniper": sniper_bot,
            "cyber": cyber_sec, "repair": repair_bot, "integrator": integrator_bot,
            "hand": hand_agent, "vision": vision_bot, "ears": ear_bot, "voice": voice_bot,
            "web": web_nav_bot, "detective": osint_bot, "media": social_bot, "safety": safety_bot,
            "creator": content_bot, "style": stylist_bot, "file": file_bot,
            "ayurveda": ayurveda_expert, "mythology": mythology_expert, "memory": memory_bot
        }

    def process_command(self, user_input, file_data=None):
        cmd = user_input.lower()

        # १. सबसे पहले सुरक्षा की जाँच (Security Check)
        if any(x in cmd for x in ["hack", "हमला", "खतरा"]):
            return clean_shiv_response(self.army["ghost"].deploy_honeypot() + self.army["repair"].fix_code())

        # २. कोडिंग, फाइल बनाना और सजावट (Coding & Auto-Style)
        if any(x in cmd for x in ["code", "लिखो", "बनाओ", "बग", "सजाओ"]):
            raw_code = self.army["coding"].execute_task(user_input)
            return self.army["style"].beautify_content("कोडिंग अपडेट", [raw_code])

        # ३. मोबाइल और एंड्रॉइड इंटीग्रेशन (Android Integration)
        if any(x in cmd for x in ["मोबाइल", "कॉल", "एंड्रॉइड", "नोटिफिकेशन"]):
            return clean_shiv_response(self.army["integrator"].sync_device("Android"))

        # ४. लोकेशन और डिटेक्टिव कार्य (Detective/OSINT)
        if any(x in cmd for x in ["लोकेशन", "trace", "ip", "पता लगाओ"]):
            return clean_shiv_response(self.army["detective"].trace_location(user_input))

        # ५. फाइल अपलोड और मैनेजमेंट (File/Upload)
        if file_data or "अपलोड" in cmd:
            return clean_shiv_response(self.army["file"].handle_upload(file_data or "unknown_file"))

        # ६. आयुर्वेद और पुराण (Heritage Knowledge)
        if any(x in cmd for x in ["इलाज", "दोष", "पुराण", "कथा"]):
            if "पुराण" in cmd: return clean_shiv_response(self.army["mythology"].get_myth_content(user_input))
            return clean_shiv_response(self.army["ayurveda"].get_treatment_logic(user_input))

        # ७. वेब और सोशल मीडिया (Web/Media)
        if any(x in cmd for x in ["सर्च", "यूट्यूब", "फेसबुक", "खोजो"]):
            return clean_shiv_response(self.army["web"].navigate_and_action("https://google.com", "search", user_input))

        # ८. डिजिटल हाथ (Hand Control)
        if any(x in cmd for x in ["क्लिक", "ड्रैग", "पकड़ो"]):
            return clean_shiv_response(self.army["hand"].type_command(user_input))

        # ९. अगर कुछ समझ न आए तो एआई दिमाग (Core Brain)
        from app.services.groq_service import get_shiv_response
        return clean_shiv_response(get_shiv_response(user_input))

# हब को एक्टिवेट करना
shiv_hub = ShivAIHub()
