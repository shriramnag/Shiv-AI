# ****************************************************************************
# प्रोजेक्ट: शिव एआई (SHIV AI) | मालिक: श्री राम नाग (Shri Ram nag)
# फाइल: main.py (The Security-First Engine)
# ****************************************************************************

import subprocess
import sys
import os
import time
from config import config # आपकी नई सुरक्षा फाइल

def check_system_integrity():
    """सिस्टम की सुरक्षा और फाइलों की जाँच करना"""
    print(f"🔱 {config.ai_name} जाग्रत हो रहा है...")
    time.sleep(1)

    # १. सुरक्षा जाँच (API Keys की निगरानी)
    if not config.validate_security():
        print("❌ सिस्टम रुक गया है। कृपया अपनी .env फाइल में असली चाबियाँ डालें।")
        sys.exit(1)

    # २. जरूरी डायरेक्टरी की जाँच
    folders = ['app/services', 'app/utils', 'app/uploads', 'app/assets/voice_samples']
    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"📁 फोल्डर बनाया गया: {folder}")

    # ३. हकलाने से रोकने वाले यूटिलिटी की जाँच
    if not os.path.exists('app/utils/response_formatter.py'):
        print("⚠️ चेतावनी: 'response_formatter' गायब है, नंबर हकला सकते हैं।")

    print(f"✅ मालिक {config.owner}, सभी ३२+ बॉट्स लिंक होने के लिए तैयार हैं।")

def launch_interface():
    """रिस्पॉन्सिव इंटरफेस (Streamlit) को शुरू करना"""
    print(f"🚀 {config.ai_name} अब लाइव हो रहा है (टर्बो मोड)...")
    
    # के अनुसार मोबाइल और डेस्कटॉप के लिए बेस्ट सेटिंग्स
    cmd = [
        "streamlit", "run", "app.py",
        "--server.port", "8501",
        "--theme.base", "dark",
        "--client.toolbarMode", "hidden"
    ]
    
    try:
        subprocess.run(cmd, check=True)
    except KeyboardInterrupt:
        print(f"\n🔱 प्रणाम {config.owner} जी, शिव एआई अब विश्राम कर रहा है।")
    except Exception as e:
        print(f"🚨 गंभीर एरर: {str(e)}")

if __name__ == "__main__":
    # पहले सुरक्षा चेक करो, फिर लॉन्च करो
    check_system_integrity()
    launch_interface()
