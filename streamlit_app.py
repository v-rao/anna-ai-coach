import streamlit as st
import json
import os
from anna_agent import AnnaAgent
from logger import ConversationLogger

st.set_page_config(page_title="Anna - Startup Coach", page_icon="💡")

# Ensure logs folder exists
os.makedirs("logs", exist_ok=True)

LOG_FILE = "logs/web_session_log.json"

# Load previous chat history from file
if os.path.exists(LOG_FILE):
    try:
        with open(LOG_FILE, "r") as f:
            saved_history = json.load(f)
    except json.JSONDecodeError:
        saved_history = []
else:
    saved_history = []

# Initialize Anna and logger
if "anna" not in st.session_state:
    st.session_state.anna = AnnaAgent(kb_path="kb/knowledge_base.txt")
if "logger" not in st.session_state:
    st.session_state.logger = ConversationLogger(LOG_FILE)
if "chat_history" not in st.session_state:
    # Load saved chat history into session state
    st.session_state.chat_history = []
    for turn in saved_history:
        st.session_state.chat_history.append(("You", turn["user"]))
        st.session_state.chat_history.append(("Anna", f"{turn['anna']}  \n*Reasoning:* {turn['reasoning']}"))

st.title("💡 Anna — Your Startup Coach")
st.write("Ask me anything about starting a business!")

# Chat input
user_input = st.chat_input("Type your question...")

if user_input:
    response, reasoning = st.session_state.anna.respond(user_input)
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Anna", f"{response}  \n*Reasoning:* {reasoning}"))
    st.session_state.logger.log_turn(user_input, response, reasoning)

# Display chat history
for speaker, msg in st.session_state.chat_history:
    st.markdown(f"**{speaker}:** {msg}")
