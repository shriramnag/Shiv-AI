import streamlit as st
from transformers import pipeline
import requests
import json

# १. पेज और स्टाइल सेटअप
st.set_page_config(page_title="Shiv AI Master", page_icon="🚩", layout="wide")
st.markdown("<style>.stButton>button {background-color: #28a745; color: white; border-radius: 10px;}</style>", unsafe_allow_stdio=True)

OWNER = "Shri Ram nag" #
RAW_GITHUB_URL = "https://raw.githubusercontent.com/shriramnag/Shiv-AI/main/README.md"

# २. एआई दिमाग (कोलाब वाला स्मॉल मॉडल - टर्बो स्पीड के लिए)
@st.cache_resource
def load_model():
    return pipeline("text-generation", model="HuggingFaceTB/SmolLM2-135M-Instruct")

pipe = load_model()

# ३. गिटहब से नॉलेज पढ़ना (जैसे कोलाब में हो रहा था)
def get_github_knowledge():
    try:
        response = requests.get(RAW_GITHUB_URL)
        return response.text[:1000] if response.status_code == 200 else "Knowledge not found."
    except:
        return "Connection Error."

# ४. हिंदी नंबर क्लीनर (हकलाना बंद करने के लिए)
def clean_text(text):
    n_map = {"1":"एक", "2":"दो", "3":"तीन", "4":"चार", "5":"पाँच", "0":"शून्य"}
    for n, w in n_map.items():
        text = text.replace(n, w)
    return text

# ५. ३२ बॉट्स और ट्रेनिंग कंट्रोल
st.title("🚩 शिव एआई (Shiv AI) - गिटहब कनेक्टेड")
st.sidebar.header("🛠️ कंट्रोल सेंटर")
st.sidebar.write(f"**मालिक:** {OWNER}")

# ट्रेनिंग लिंक (कोलाब के लिए)
colab_link = "https://colab.research.google.com/github/shriramnag/Shiv-AI/blob/main/ShivAi.ipynb"
st.sidebar.markdown(f"[🔥 कोलाब पर ट्रेन करें]({colab_link})")

# ३२ बॉट्स सेलेक्टर
bot_list = [f"बॉट {i+1}" for i in range(32)]
selected_bot = st.sidebar.selectbox("अपना बॉट चुनें:", bot_list)

# ६. चैट इंटरफेस (कोलाब जैसा लुक)
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_input = st.chat_input("श्री राम नाग जी, यहाँ आदेश लिखें...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant"):
        knowledge = get_github_knowledge()
        input_fixed = clean_text(user_input)
        
        # प्रोम्प्ट इंजीनियरिंग (कोलाब वाला सिस्टम प्रोम्प्ट)
        sys_prompt = f"You are Shiv AI, created by {OWNER}. Active Bot: {selected_bot}. Knowledge: {knowledge}. Answer shortly in Hindi."
        full_prompt = f"<|system|>\n{sys_prompt}<|user|>\n{input_fixed}<|assistant|>\n"
        
        res = pipe(full_prompt, max_new_tokens=100, do_sample=True, temperature=0.4)
        response = res[0]['generated_text'].split("<|assistant|>\n")[-1].strip()
        
        st.write(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
