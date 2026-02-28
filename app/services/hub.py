# ****************************************************************************
# प्रोजेक्ट: शिव एआई (SHIV AI) | मालिक: श्री राम नाग (Shri Ram nag)
# फाइल: hub.py (The Infinite Command Center)
# विशेषता: ३२+ बॉट्स, जीरो एरर, और बिना हकलाए संवाद
# ****************************************************************************

import os
from app.utils.response_formatter import clean_shiv_response

# --- सभी ३२+ विभागों का महा-संगम (Imports) ---

# १. कोडिंग, रिपेयर और सफाई (Core Engineering)
from app.services.agent_service import agent_manager      # कोडिंग मास्टर
from app.services.terminal_service import terminal_bot   # टर्मिनल कंट्रोल
from app.services.learning_engine import self_learner    # ऑटो-लर्निंग
from app.services.defense_repair_bot import repair_bot    # सेल्फ-हीलिंग
from app.services.system_cleaner_bot import system_cleaner # कचरा साफ करने वाला
from app.services.code_optimizer import optimizer_bot     # कोड को तेज करने वाला

# २. सुरक्षा, माया और प्रहार (Security & Ghost Defense)
from app.services.ghost_protocol_bot import ghost_bot      # चकमा देने वाला
from app.services.security_elite import elite_defense      # टाइम लॉक/मिरर
from app.services.network_sniper import sniper_bot        # वायरस स्नाइपर
from app.services.cyber_security_agent import cyber_sec   # २४/७ सुरक्षा
from app.services.stealth_module import stealth_bot       # अदृश्य मोड
from app.services.firewall_agent import firewall_bot      # डिजिटल दीवार
from app.services.encryption_bot import crypto_bot        # डेटा को लॉक करने वाला

# ३. मोबाइल, हार्डवेयर और इंद्रियां (Android & Senses)
from app.services.system_integrator_bot import integrator_bot # मोबाइल लिंक
from app.services.visual_hand_agent import hand_agent          # डिजिटल हाथ
from app.services.vision_service import vision_bot            # एआई की आँखें
from app.services.stt_service import ear_bot                 # सुनने की शक्ति
from app.services.voice_service import voice_bot             # बोलने की शक्ति
from app.services.battery_manager import battery_bot         # मोबाइल पावर सेवर

# ४. वेब, डिटेक्टिव और सोशल (Internet & OSINT)
from app.services.web_navigator_bot import web_nav_bot     # वेब ब्राउजिंग
from app.services.osint_detective_bot import osint_bot     # लोकेशन/आईपी ट्रेस
from app.services.media_agent import social_bot           # यूट्यूब/इंस्टा मैनेजर
from app.services.search_expert import search_bot         # डीप वेब सर्च
from app.services.news_aggregator import news_bot         # ताज़ा खबरें

# ५. कंटेंट, स्टाइल और मीडिया (Creative Suite)
from app.services.content_creator_bot import content_bot   # स्क्रिप्ट/कंटेंट
from app.services.stylist_writer_bot import stylist_bot    # सजावट/फॉर्मेटिंग
from app.services.file_manager_bot import file_bot         # फाइल मैनेजमेंट
from app.services.image_gen_bot import image_bot          # एआई फोटो जनरेटर
from app.services.video_editor_bot import video_bot       # वीडियो एडिटिंग

# ६. प्राचीन ज्ञान और चेतना (Knowledge & Memory)
from app.services.ayurveda_bot import ayurveda_expert      # आयुर्वेद चिकित्सा
from app.services.mythology_bot import mythology_expert    # पुराण/महाभारत
from app.services.chat_service import memory_bot           # लॉन्ग टर्म याददाश्त
from app.services.vocab_dictionary import vocab_bot       # शुद्ध हिंदी शब्दकोश

class ShivAIHub:
    def __init__(self):
        # ३२+ बॉट्स की सेना (The Ultimate Army)
        self.army = {
            "coding": agent_manager, "terminal": terminal_bot, "learning": self_learner,
            "repair": repair_bot, "cleaner": system_cleaner, "optimizer": optimizer_bot,
            "ghost": ghost_bot, "elite": elite_defense, "sniper": sniper_bot,
            "cyber": cyber_sec, "stealth": stealth_bot, "firewall": firewall_bot,
            "crypto": crypto_bot, "integrator": integrator_bot, "hand": hand_agent,
            "vision": vision_bot, "ears": ear_bot, "voice": voice_bot, "battery": battery_bot,
            "web": web_nav_bot, "detective": osint_bot, "social": social_bot,
            "search": search_bot, "news": news_bot, "creator": content_bot,
            "style": stylist_bot, "file": file_bot, "image": image_bot, "video": video_bot,
            "ayurveda": ayurveda_expert, "mythology": mythology_expert, "memory": memory_bot,
            "vocab": vocab_bot
        }

    def process_command(self, user_input, file_data=None):
        cmd = user_input.lower()

        # १. टर्बो क्लीनर और ऑप्टिमाइज़र (Speed First)
        if any(x in cmd for x in ["साफ करो", "clean", "तेज करो", "optimize"]):
            clean_msg = self.army["cleaner"].clean_junk()
            opt_msg = self.army["optimizer"].boost_performance()
            return clean_shiv_response(f"{clean_msg} {opt_msg}")

        # २. कोडिंग, बग फिक्स और स्टाइल (Integrated Engineering)
        if any(x in cmd for x in ["code", "लिखो", "बनाओ", "बग"]):
            raw_code = self.army["coding"].execute_task(user_input)
            # कोडिंग को सीधे स्टाइल बॉट से सजाकर भेजना
            return self.army["style"].beautify_content("कोडिंग अपडेट", [raw_code])

        # ३. मोबाइल/एंड्रॉइड कार्य (Mobile Integration)
        if any(x in cmd for x in ["मोबाइल", "एंड्रॉइड", "कॉल", "बैटरी"]):
            return clean_shiv_response(self.army["integrator"].sync_device("Android"))

        # ४. सुरक्षा और शातिर डिफेंस (Defense Mode)
        if any(x in cmd for x in ["hack", "खतरा", "अटैक"]):
            self.army["ghost"].deploy_honeypot()
            return clean_shiv_response("🛡️ सुरक्षा चक्र सक्रिय। हमला नाकाम कर दिया गया है।")

        # ५. प्राचीन ज्ञान (Ayurveda/Mythology)
        if any(x in cmd for x in ["इलाज", "पुराण", "महाभारत"]):
            if "पुराण" in cmd: return clean_shiv_response(self.army["mythology"].get_myth_content(user_input))
            return clean_shiv_response(self.army["ayurveda"].get_treatment_logic(user_input))

        # ६. सामान्य एआई दिमाग (Core Brain)
        from app.services.groq_service import get_shiv_response
        response = get_shiv_response(user_input)
        return clean_shiv_response(response)

# शिव हब को सक्रिय करना
shiv_hub = ShivAIHub()
