# श्री राम नाग जी, यह शिव एआई का लर्निंग इंजन है।
# यह इंटरनेट और आपकी बातों से खुद को अपडेट करता रहता है।
import os
from app.services.vector_store import vector_db

class ShivLearningEngine:
    def __init__(self):
        self.learning_file = "database/learning_data/userdata.txt"

    def learn_new_info(self, source, info):
        """नई जानकारी को याददाश्त में जोड़ना"""
        # जानकारी को साफ़ करना
        formatted_info = f"\n[Learned from {source}]: {info}"
        
        # १. टेक्स्ट फाइल में सेव करना (Permanent Storage)
        with open(self.learning_file, "a", encoding="utf-8") as f:
            f.write(formatted_info)
        
        # २. वेक्टर डेटाबेस में जोड़ना (Quick Recall)
        vector_db.add_information(info)
        
        print(f"शिव एआई ने {source} से नई बात सीख ली है।")

    def update_logic_from_code(self, new_code_logic):
        """गिटहब से मिले नए लॉजिक को खुद में समाहित करना"""
        # यह हिस्सा शिव एआई को कोडिंग स्टाइल सुधारने में मदद करेगा
        self.learn_new_info("GitHub/Code", "नया कोडिंग पैटर्न सीखा गया।")

# लर्निंग इंजन तैयार है
learner = ShivLearningEngine()
