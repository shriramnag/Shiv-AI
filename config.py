# ****************************************************************************
# प्रोजेक्ट: शिव एआई (SHIV AI) | फाइल: config.py (Security Monitor)
# ****************************************************************************

import os
from dotenv import load_dotenv

# .env फाइल से डेटा लोड करना
load_dotenv()

class ShivConfig:
    def __init__(self):
        self.owner = os.getenv("OWNER_NAME", "Shri Ram nag")
        self.ai_name = os.getenv("AI_NAME", "Shiv AI")
        self.api_key = os.getenv("GRQ_API_KEY")
        self.security_level = os.getenv("SECURITY_LEVEL", "elite")

    def validate_security(self):
        """चाबियों की सुरक्षा जाँच (Monitoring)"""
        if not self.api_key or "here" in self.api_key or "यहाँ" in self.api_key:
            print(f"🚨 सुरक्षा अलर्ट: {self.owner} जी, आपकी API Key सुरक्षित नहीं है!")
            return False
        
        print(f"✅ सुरक्षा चक्र सक्रिय: {self.ai_name} पूरी तरह सुरक्षित है।")
        return True

# ग्लोबल कॉन्फ़िगरेशन ऑब्जेक्ट
config = ShivConfig()
