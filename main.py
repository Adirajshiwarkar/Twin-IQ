import os

import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

st.set_page_config(
    page_title="Chat with Gemini-Pro!",
    page_icon="virus:",
)

GOOGLE_API_KEY = os.getenv("AIzaSyAyn8S0lG2CVhFbrdYaV9QdbKxu4TID4E0")

genai.configure(api_key="AIzaSyAyn8S0lG2CVhFbrdYaV9QdbKxu4TID4E0")
model = genai.GenerativeModel('models/gemini-1.5-flash-latest')


def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role


if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

st.title("🧠⇄🧠 TwinIQ ")

for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
        st.markdown(message.parts[0].text)

user_prompt = st.chat_input("👋 “Hi! I’m TwinIQ, your smart AI assistant —Let’s explore your "
                            "questions together!”")
if user_prompt:
    st.chat_message("user").markdown(user_prompt)

    gemini_response = st.session_state.chat_session.send_message(user_prompt)

    with st.chat_message("assistant"):
        st.markdown(gemini_response.text)
