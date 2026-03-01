import streamlit as st
from transformers import pipeline
from gtts import gTTS
import base64
import os
import requests

# १. पेज सेटअप और मास्टर लॉक
st.set_page_config(page_title="Shiv AI - Master Control", page_icon="🚩", layout="wide")
OWNER = "Shri Ram nag" #
AI_NAME = "Shiv AI"
COLAB_URL = "https://colab.research.google.com/github/shriramnag/Shiv-AI/blob/main/ShivAi.ipynb"

# २. एआई दिमाग (टर्बो स्पीड)
@st.cache_resource
def load_shiv_brain():
    return pipeline("text-generation", model="HuggingFaceTB/SmolLM2-135M-Instruct")

pipe = load_shiv_brain()

# ३. आवाज़ और नंबर फिक्सर (हकलाना बंद करने के लिए)
def get_voice_html(text):
    # नंबर को शब्दों में बदलें ताकि आवाज़ साफ़ आए
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

# ४. साइडबार - ३२ बॉट्स और पुराने टूल्स
st.sidebar.title(f"🚩 {AI_NAME} कंट्रोल")
st.sidebar.write(f"**मालिक:** {OWNER}")

# एंटी-स्लीपिंग कोलाब लिंक (पुराना टूल वापस आ गया)
st.sidebar.markdown(f"""
    <a href="{COLAB_URL}" target="_blank">
        <button style="width:100%; border-radius:10px; background-color:#ff4b4b; color:white; padding:10px; border:none; cursor:pointer;">
            🚀 कोलाब एक्टिवेटर (Anti-Sleep)
        </button>
    </a>
    """, unsafe_allow_stdio=True)

# ३२ बॉट्स की चाबी (कनेक्शन)
bot_list = [f"बॉट {i+1}" for i in range(32)]
selected_bot = st.sidebar.selectbox("अपना बॉट चुनें:", bot_list)
st.sidebar.success(f"✅ {selected_bot} कनेक्टेड है")

# ५. मुख्य चैट और आवाज़ का जादू
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

user_input = st.chat_input("श्री राम नाग जी, आदेश दें...")

if user_input:
    with st.chat_message("user"):
        st.write(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # एआई लॉजिक
    sys_msg = f"You are {AI_NAME} by {OWNER}. Active Bot: {selected_bot}. Turbo speed. Answer in Hindi."
    prompt = f"<|system|>\n{sys_msg}<|user|>\n{user_input}<|assistant|>\n"
    
    res = pipe(prompt, max_new_tokens=60, do_sample=True, temperature=0.5)
    response = res[0]['generated_text'].split("<|assistant|>\n")[-1].strip()

    with st.chat_message("assistant"):
        st.write(response)
        # आवाज़ सुनाएं (जान डालना)
        st.markdown(get_voice_html(response), unsafe_allow_stdio=True)
    
    st.session_state.messages.append({"role": "assistant", "content": response})
