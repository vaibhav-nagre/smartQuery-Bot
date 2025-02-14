# conda activate smartQueryBot
#pip install streamlit langchain langchain-openai

import streamlit as st

st.set_page_config(
    page_title="Smart Query Bot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("Smart Query Bot")

with st.sidebar:
    st.header("Settings")
    website_url = st.text_input("Website URL")

st.chat_input("Ask me anything")

with st.chat_message("AI"):
    st.write("I am a smart query bot. I can answer your questions. Ask me anything.")

with st.chat_message("user"):
    st.write("What is the weather today?")