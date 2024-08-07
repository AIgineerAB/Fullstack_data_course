import streamlit as st
import pandas as pd
from pathlib import Path
from bot import Bot

def initialize_session_state():
    """Initialize session state variables."""
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "bot" not in st.session_state:
        st.session_state.bot = Bot()

def display_chat_messages():
    """Display chat messages from history"""
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

def handle_user_input():
    """Handle user input and generate bot response."""
    if prompt := st.chat_input("What is up?"):

        with st.chat_message("user"):
            st.markdown(prompt)

        st.session_state.messages.append({"role": "user", "content": prompt})

        bot_response = st.session_state.bot.chat(prompt)
        response = f"Ro Båt: {bot_response}"

        with st.chat_message("assistant"):
            st.markdown(response)

        st.session_state.messages.append({"role": "assistant", "content": response})

def layout():
    """Define the layout of the Streamlit app."""
    st.title("Chatting with RO BÅT")
    st.write("RO BÅT is a funny robot that can help you out with programming tasks. However he doesn't directly answer your question, usually he asks another question back.")
    display_chat_messages()
    handle_user_input()

if __name__ == "__main__":
    initialize_session_state()
    layout()