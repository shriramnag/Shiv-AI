import streamlit as st
from transformers import pipeline
from gtts import gTTS
import base64
import os

# १. पेज सेटअप और टाइटल
st.set_page_config(page_title="Shiv AI - Voice Update", page_icon="🚩")
OWNER = "Shri Ram nag" #

# २. वॉइस इंजन (नंबर फिक्सर के साथ ताकि हकलाए नहीं)
def get_audio_html(text):
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

# ३. एआई दिमाग (टर्बो स्पीड)
@st.cache_resource
def load_model():
    return pipeline("text-generation", model="HuggingFaceTB/SmolLM2-135M-Instruct")

pipe = load_model()

# ४. इंटरफेस (UI) और ३२ बॉट्स की चाबी
st.title("🚩 शिव एआई (Shiv AI) - वॉइस मास्टर")
st.write(f"स्वागत है, **{OWNER}** जी!")

if "messages" not in st.session_state:
    st.session_state.messages = []

# ५. चैट और वॉइस आउटपुट
user_input = st.chat_input("यहाँ अपना आदेश लिखें...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    sys_prompt = f"You are Shiv AI by {OWNER}. You have 32 bots. Answer shortly in Hindi."
    full_prompt = f"<|system|>\n{sys_prompt}<|user|>\n{user_input}<|assistant|>\n"
    
    res = pipe(full_prompt, max_new_tokens=60, do_sample=True, temperature=0.5)
    response = res[0]['generated_text'].split("<|assistant|>\n")[-1].strip()
    
    st.session_state.messages.append({"role": "assistant", "content": response})
    
    # आवाज़ सुनाएं
    audio_html = get_audio_html(response)
    st.markdown(audio_html, unsafe_allow_stdio=True)

# चैट डिस्प्ले
for msg in reversed(st.session_state.messages):
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
