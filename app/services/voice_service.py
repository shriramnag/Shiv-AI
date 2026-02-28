# ****************************************************************************
# प्रोजेक्ट: शिव एआई (SHIV AI) | मालिक: श्री राम नाग
# विभाग: कस्टम वॉइस क्लोनिंग (No ElevenLabs, 100% Free)
# ****************************************************************************

import os
from TTS.api import TTS

class CustomVoiceService:
    def __init__(self):
        # हम 'xtts_v2' जैसे फ्री मॉडल का उपयोग करेंगे जो सैंपल से आवाज बदलता है
        self.model_name = "tts_models/multilingual/multi-dataset/xtts_v2"
        self.sample_path = "app/assets/voice_samples/shri_ram_nag.wav"
        self.output_path = "Shri Ram Nag.wav" #

    def speak(self, text):
        """सैंपल फाइल का उपयोग करके आवाज बनाना"""
        # के अनुसार नंबरों को हिंदी में बदला जाएगा
        try:
            tts = TTS(self.model_name).to("cpu") # मोबाइल के लिए CPU या GPU
            tts.tts_to_file(
                text=text,
                speaker_wav=self.sample_path,
                language="hi",
                file_path=self.output_path
            )
            return f"आवाज फाइल '{self.output_path}' तैयार है, मालिक।"
        except Exception as e:
            return f"वॉइस एरर: {str(e)}"

voice_bot = CustomVoiceService()
