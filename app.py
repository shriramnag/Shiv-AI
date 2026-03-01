import streamlit as st
from transformers import pipeline
import requests
from gtts import gTTS
import os
import base64

# १. पेज सेटअप
st.set_page_config(page_title="Shiv AI - Voice Control", page_icon="🚩")

OWNER = "Shri Ram nag" #
COLAB_URL = "https://colab.research.google.com/github/shriramnag/Shiv-AI/blob/main/ShivAi.ipynb"

# २. एआई दिमाग और आवाज़ का सिस्टम
@st.cache_resource
def load_shiv_brain():
    return pipeline("text-generation", model="HuggingFaceTB/SmolLM2-135M-Instruct")

pipe = load_shiv_brain()

def get_audio_html(text):
    # नंबर फिक्सर ताकि आवाज़ साफ़ आए
    n_map = {"1":"एक", "2":"दो", "3":"तीन", "4":"चार", "5":"पाँच", "0":"शून्य"}
    for n, w in n_map.items():
        text = text.replace(n, w)
    
    tts = gTTS(text, lang='hi')
    filename = "Shri Ram Nag.wav" #
    tts.save(filename)
    
    with open(filename, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        return f'<audio autoplay="true" src="data:audio/wav;base64,{b64}">'

# ३. मुख्य इंटरफेस (UI)
st.title("🚩 शिव एआई (Shiv AI) - वॉइस अपडेट")
st.sidebar.title("🛠️ कंट्रोल सेंटर")
st.sidebar.write(f"**मालिक:** {OWNER}")

# कोलाब ट्रेनिंग और एक्टिवेशन बटन
st.sidebar.markdown(f"""
    <a href="{COLAB_URL}" target="_blank">
        <button style="width:100%; border-radius:10px; background-color:#f9ab00; color:white; padding:10px; border:none; cursor:pointer;">
            🔥 कोलाब पर एक्टिवेट करें
        </button>
    </a>
    """, unsafe_allow_stdio=True)

# ४. चैट और आवाज़ का जादू
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.chat_input("श्री राम नाग जी, यहाँ आदेश लिखें...")

if user_input:
    with st.spinner("शिव एआई सुन रहा है..."):
        # एआई रिस्पॉन्स
        sys_msg = f"You are Shiv AI by {OWNER}. Answer shortly in Hindi."
        prompt = f"<|system|>\n{sys_msg}<|user|>\n{user_input}<|assistant|>\n"
        res = pipe(prompt, max_new_tokens=60, do_sample=True, temperature=0.5)
        response = res[0]['generated_text'].split("<|assistant|>\n")[-1].strip()
        
        # आवाज़ सुनाएं
        audio_html = get_audio_html(response)
        st.markdown(audio_html, unsafe_allow_stdio=True)
        
        # चैट दिखाएं
        st.session_state.chat_history.append({"user": user_input, "bot": response})

for chat in reversed(st.session_state.chat_history):
    st.write(f"👤 **आप:** {chat['user']}")
    st.success(f"🚩 **शिव एआई:** {chat['bot']}")
    
