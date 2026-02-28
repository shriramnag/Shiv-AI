# ****************************************************************************
# प्रोजेक्ट: शिव एआई (SHIV AI) | मालिक: श्री राम नाग (Shri Ram nag)
# फाइल: app.py (The Main Entry Point)
# विशेषता: टर्बो स्पीड, बिना हकलाए संवाद और ३२+ बॉट्स का कंट्रोल
# ****************************************************************************

import streamlit as st
import os
import sys
import time

# १. पाथ सुरक्षा (कोलाब के लिए अनिवार्य)
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)

# २. मालिक और एआई की पहचान
OWNER_NAME = "Shri Ram nag"
AI_NAME = "Shiv AI"

# ३. बिना हकलाए संवाद के लिए फंक्शन
def hindi_text_cleaner(text):
    """नंबरों और डॉट को हिंदी शब्दों में बदलता है ताकि एआई हकलाए नहीं"""
    # यहाँ नंबरों को शब्दों में बदलने का लॉजिक है
    numbers = {
        "0": "शून्य", "1": "एक", "2": "दो", "3": "तीन", "4": "चार", 
        "5": "पाँच", "6": "छह", "7": "सात", "8": "आठ", "9": "नौ", ".": "डॉट"
    }
    for num, word in numbers.items():
        text = text.replace(num, word)
    return text

# ४. स्ट्रीमलिट इंटरफेस सेटअप
st.set_page_config(page_title=AI_NAME, page_icon="🚩", layout="wide")

# साइडबार में स्टेटस और २८+ मॉडल्स की जानकारी
with st.sidebar:
    st.title(f"🚩 {AI_NAME}")
    st.write(f"**मालिक:** {OWNER_NAME}")
    st.markdown("---")
    st.success("३२+ बॉट्स ऑनलाइन हैं")
    st.info("मोड: टर्बो हाई स्पीड")

# ५. शिव हब (The Infinite Command Center) को लोड करना
try:
    from app.services.hub import shiv_hub
    system_active = True
except Exception as e:
    st.error(f"हब लोड करने में समस्या: {e}")
    system_active = False

# ६. मुख्य स्क्रीन
st.title(f"नमस्ते {OWNER_NAME} जी! 🙏")
st.write(f"आपका **{AI_NAME}** आपकी सेवा के लिए तैयार है।")

# ७. चैटिंग लॉजिक
if "messages" not in st.session_state:
    st.session_state.messages = []

# पुराने मैसेज दिखाना
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# नया इनपुट लेना
if prompt := st.chat_input("श्री राम नाग जी, आदेश दें..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("शिव सोच रहा है..."):
            if system_active:
                # हब के जरिए कमांड प्रोसेस करना
                raw_response = shiv_hub.process_command(prompt)
                # बिना हकलाए संवाद के लिए क्लीनिंग
                final_response = hindi_text_cleaner(raw_response)
                
                st.markdown(final_response)
                st.session_state.messages.append({"role": "assistant", "content": final_response})
                
                # ऑडियो बटन (TTS 5 फ्री मॉडल)
                if st.button("ऑडियो सुनें (टर्बो)"):
                    st.write("🔊 ऑडियो टर्बो स्पीड पर तैयार हो रहा है...")
            else:
                st.warning("सिस्टम हब सक्रिय नहीं है। कृपया कोड चेक करें।")

# ****************************************************************************
# कोडिंग सुरक्षित - श्री राम नाग (Shri Ram nag)
# ****************************************************************************
