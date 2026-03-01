import streamlit as st

# १. बेसिक सेटअप
st.set_page_config(page_title="Shiv AI - Control Center", page_icon="🚩")
OWNER = "Shri Ram nag" #
COLAB_LINK = "https://colab.research.google.com/github/shriramnag/Shiv-AI/blob/main/ShivAi.ipynb"

# २. हेडर और स्टेटस
st.title("🚩 शिव एआई (Shiv AI) कंट्रोल पैनल")
st.write(f"**स्वागत है, {OWNER} जी!**")

# ३. ट्रेनिंग सेक्शन (यही आप चाहते थे)
st.info("💡 यहाँ से आप सीधे कोलाब पर जाकर मॉडल ट्रेन कर सकते हैं।")
if st.button("🔥 कोलाब में ट्रेनिंग शुरू करें"):
    st.markdown(f'<meta http-equiv="refresh" content="0;URL=\'{COLAB_LINK}\'" />', unsafe_allow_stdio=True)
    st.write("कोलाब खुल रहा है... कृपया इंतज़ार करें।")

# ४. प्रोजेक्ट स्टेटस
st.sidebar.title("📊 प्रोजेक्ट स्टेटस")
st.sidebar.markdown(f"""
- **मालिक:** {OWNER}
- **बॉट्स:** ३२ एक्टिव
- **स्पीड:** टर्बो हाई
- **मोड:** एंटी-स्लीप ऑन
""")
