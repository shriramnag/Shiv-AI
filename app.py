# ****************************************************************************
# प्रोजेक्ट: शिव एआई (SHIV AI) | मालिक: श्री राम नाग (Shri Ram nag)
# अपडेट: डेवलपर फूटर और रिस्पॉन्सिव डिजाइन
# ****************************************************************************

import streamlit as st
import time
from app.services.hub import shiv_hub 
from config import config # कॉन्फ़िग से नाम लेने के लिए

# १. पेज सेटिंग्स
st.set_page_config(page_title=f"{config.ai_name} - {config.owner}", page_icon="🔱", layout="wide")

# २. रिस्पॉन्सिव CSS और फूटर स्टाइल
st.markdown("""
    <style>
    .main { background-color: #0E1117; color: #FFFFFF; }
    
    /* फूटर की सजावट */
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #1E1E1E;
        color: #4CAF50;
        text-align: center;
        padding: 10px;
        font-size: 14px;
        font-weight: bold;
        border-top: 1px solid #4CAF50;
        z-index: 100;
    }
    
    /* मोबाइल के लिए चैट स्पेसिंग */
    @media (max-width: 640px) {
        .stChatFloatingInputContainer { bottom: 60px !important; }
        .main .block-container { padding-bottom: 100px !important; }
    }
    </style>
    """, unsafe_allow_html=True)

# ३. मुख्य हेडर
st.title(f"🔱 {config.ai_name}")
st.write(f"स्वागत है, **{config.owner}** जी।") #

# --- चैट लॉजिक यहाँ रहेगा ---
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("आदेश दें, मालिक..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = shiv_hub.process_command(prompt)
        
        # टाइपिंग इफेक्ट (बिना हकलाए)
        displayed_text = ""
        for char in full_response:
            displayed_text += char
            response_placeholder.markdown(displayed_text + "▌")
            time.sleep(0.01)
        response_placeholder.markdown(full_response)
    
    st.session_state.messages.append({"role": "assistant", "content": full_response})

# ४. डेवलपर फूटर (The Professional Signature)
st.markdown(f"""
    <div class="footer">
        🚀 Developed with ❤️ by {config.owner} | Shiv AI v2.0 Turbo
    </div>
    """, unsafe_allow_html=True)
