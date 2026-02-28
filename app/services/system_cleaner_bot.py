# ****************************************************************************
# प्रोजेक्ट: शिव एआई (SHIV AI) | मालिक: श्री राम नाग (Shri Ram nag)
# विभाग: सिस्टम ऑप्टिमाइजेशन और क्लीनर
# ****************************************************************************

import os
import shutil

class SystemCleanerBot:
    def __init__(self):
        self.owner = "Shri Ram nag"
        self.temp_folders = ["app/uploads/temp", "__pycache__"]

    def clean_junk(self):
        """फालतू फाइलों और कैश को साफ करना"""
        print(f"मालिक {self.owner}, मैं सिस्टम का कचरा साफ कर रहा हूँ...")
        cleaned_count = 0
        
        # पायथन कैश साफ करना
        for root, dirs, files in os.walk('.'):
            for d in dirs:
                if d == "__pycache__":
                    shutil.rmtree(os.path.join(root, d))
                    cleaned_count += 1
        
        return f"सफलता! मैंने {cleaned_count} कचरा फाइलों को हटा दिया है। अब आपका सिस्टम टर्बो स्पीड पर है।"

system_cleaner = SystemCleanerBot()
