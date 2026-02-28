# ****************************************************************************
# प्रोजेक्ट: शिव एआई (SHIV AI) | मालिक: श्री राम नाग (Shri Ram nag)
# स्थान: रूट डायरेक्टरी (Root Directory)
# ****************************************************************************

import streamlit as st
import time
# रूट से सर्विसेस को इम्पोर्ट करना
from app.services.hub import shiv_hub 

# स्मार्ट रिस्पॉन्सिव कॉन्फ़िगरेशन
st.set_page_config(page_title="Shiv AI - Shri Ram Nag", page_icon="🔱", layout="wide")

# कस्टम सीएसएस: मोबाइल और डेस्कटॉप के लिए अलग-अलग लुक
st.markdown("""
    <style>
    .main { background-color: #0E1117; color: #FFFFFF; }
    @media (max-width: 640px) { .stChatMessage { font-size: 14px !important; } }
    .stButton>button { border-radius: 20px; background-color: #1E1E1E; color: white; border: 1px solid #4CAF50; }
    </style>
    """, unsafe_allow_html=True)

st.title("🔱 शिव एआई (Shiv AI)")
st.write(f"स्वागत है, **श्री राम नाग** जी। सिस्टम ऑनलाइन है।")

if "messages" not in st.session_state:
    st.session_state.messages = []

# चैट हिस्ट्री दिखाना
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# इनपुट बॉक्स
if prompt := st.chat_input("आदेश दें, मालिक..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        # हब के माध्यम से २७+ बॉट्स को कमांड भेजना
        full_response = shiv_hub.process_command(prompt)
        
        # बिना हकलाए टाइपिंग इफेक्ट
        displayed_text = ""
        for char in full_response:
            displayed_text += char
            response_placeholder.markdown(displayed_text + "▌")
            time.sleep(0.01)
        response_placeholder.markdown(full_response)
    
    st.session_state.messages.append({"role": "assistant", "content": full_response})

# मोबाइल और डेस्कटॉप के लिए कंट्रोल पैनल
with st.sidebar:
    st.header("⚙️ कंट्रोल सेंटर")
    st.info("डिवाइस: ऑटो-डिटेक्ट सक्रिय")
    uploaded_file = st.file_uploader("स्क्रीनशॉट या कोड अपलोड करें", type=['png', 'jpg', 'py', 'txt'])
    if uploaded_file:
        st.success(f"फाइल '{uploaded_file.name}' सुरक्षित रूप से प्राप्त हुई।")
    st.divider()
    st.write("डेवलपर: **Shri Ram nag**")
  
