import os
import json 
import streamlit as st
import google.generativeai as genai
import PIL.Image

# Load Gemini API key from config.json
working_dir = os.path.dirname(os.path.abspath(__file__))
config_data = json.load(open(f"{working_dir}/config.json"))
GEMINI_API_KEY = config_data["GEMINI_API_KEY"]

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

# Streamlit setup
st.set_page_config(
    page_title="Gemini-1.5-fusion GPT Chat",
    page_icon="🗣",
    layout="centered"
)
st.title("🤖 Boring ChatBot")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display past messages
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Get user input
user_prompt = st.chat_input("Ask Gemini 1.5....")

if user_prompt:
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role": "user", "content": user_prompt})

    # Create Gemini chat model + attach history
    model = genai.GenerativeModel("gemini-1.5-flash")  # or gemini-1.5-pro
    chat = model.start_chat(history=[
        {"role": m["role"], "parts": [m["content"]]} for m in st.session_state.chat_history
    ])

    # Get response
    response = chat.send_message(user_prompt)
    assistant_response = response.text

    # Save & show response
    st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})
    with st.chat_message("assistant"):
        st.markdown(assistant_response)