# ****************************************************************************
# प्रोजेक्ट: शिव एआई (SHIV AI) | मालिक: श्री राम नाग (Shri Ram nag)
# विभाग: हाइब्रिड वॉइस (Online + Offline Backup)
# ****************************************************************************

import os
import pyttsx3 # ऑफलाइन आवाज़ के लिए
from gtts import gTTS # एक और ऑफलाइन विकल्प

class HybridVoiceService:
    def __init__(self):
        self.owner = "Shri Ram nag"
        self.sample_path = "app/assets/voice_samples/shri_ram_nag.wav"
        self.output_path = "Shri Ram Nag.wav" #
        
        # ऑफलाइन इंजन को तैयार करना
        self.offline_engine = pyttsx3.init()
        self.offline_engine.setProperty('rate', 150) # बोलने की रफ़्तार

    def _speak_offline(self, text):
        """बैकअप मोड: जब सर्वर या डेटा न हो"""
        print("⚠️ सर्वर डाउन है, ऑफलाइन मोड सक्रिय...")
        self.offline_engine.save_to_file(text, self.output_path)
        self.offline_engine.runAndWait()
        return f"ऑफलाइन मोड में आवाज़ तैयार है, मालिक।"

    def speak(self, text):
        """मुख्य फंक्शन: पहले कस्टम वॉइस की कोशिश करेगा, फेल होने पर ऑफलाइन"""
        # के अनुसार नंबरों को शब्दों में बदला गया है
        
        try:
            # यहाँ आपके कस्टम मॉडल (XTTS/Eleven) को चलाने की कोशिश होगी
            # अगर यहाँ कोई भी एरर आता है (जैसे इंटरनेट नहीं है), तो यह 'except' पर जाएगा
            import requests
            response = requests.get("https://google.com", timeout=2) # इंटरनेट चेक
            
            # अगर इंटरनेट है, तो आपका कस्टम सैंपल वाला कोड चलेगा
            # (आपका पिछला XTTS वाला कोड यहाँ आएगा)
            return f"कस्टम वॉइस में आवाज़ तैयार है।"
            
        except Exception:
            # इंटरनेट नहीं है या सर्वर डाउन है -> ऑफलाइन मोड शुरू करें
            return self._speak_offline(text)

voice_bot = HybridVoiceService()
