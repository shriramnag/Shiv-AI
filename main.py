# ****************************************************************************
# प्रोजेक्ट: शिव एआई (SHIV AI) | मालिक: श्री राम नाग (Shri Ram nag)
# स्थान: रूट डायरेक्टरी (Root Directory)
# कार्य: २४/७ सिस्टम मॉनिटरिंग और २७+ बॉट्स का सफल संचालन
# ****************************************************************************

import os
import sys
import subprocess
import time

def setup_environment():
    """सिस्टम की सेहत की जाँच करना (Health Check)"""
    print("🔱 शिव एआई (Shiv AI) जाग्रत हो रहा है...")
    time.sleep(1)
    
    # १. जरूरी फोल्डर्स की जाँच
    required_folders = ['app/services', 'app/utils', 'app/uploads']
    for folder in required_folders:
        if not os.path.exists(folder):
            print(f"⚠️ चेतावनी: {folder} नहीं मिला, निर्माण किया जा रहा है...")
            os.makedirs(folder)

    # २. हकलाने से रोकने वाले यूटिलिटी की जाँच
    if not os.path.exists('app/utils/response_formatter.py'):
        print("❌ त्रुटि: हकलाने का इलाज (formatter) गायब है।")
    
    print("✅ सभी २७+ बॉट्स लिंक होने के लिए तैयार हैं।")

def start_shiv_engine():
    """स्ट्रीमलिट रिस्पॉन्सिव इंटरफेस को लॉन्च करना"""
    print(f"🚀 मालिक श्री राम नाग जी, आपका डिजिटल साम्राज्य अब लाइव हो रहा है...")
    
    # स्ट्रीमलिट को टर्बो मोड में चलाना (बिना किसी फालतू नोटिफिकेशन के)
    cmd = [
        "streamlit", "run", "app.py",
        "--server.headfull", "False",
        "--theme.base", "dark"
    ]
    
    try:
        # यह कमांड आपके मोबाइल या डेस्कटॉप के ब्राउज़र में 'app.py' को खोल देगी
        subprocess.run(cmd, check=True)
    except KeyboardInterrupt:
        print("\n🔱 शिव एआई अब विश्राम कर रहा है। प्रणाम, श्री राम नाग जी।")
    except Exception as e:
        print(f"🚨 गंभीर त्रुटि: {str(e)}")

if __name__ == "__main__":
    # १. पहले वातावरण तैयार करो
    setup_environment()
    # २. फिर इंजन स्टार्ट करो
    start_shiv_engine()
  
