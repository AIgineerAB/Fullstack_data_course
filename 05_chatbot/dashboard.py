import streamlit as st
import pandas as pd
from pathlib import Path
from bot import Bot

bot = Bot()

def chat():
        # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # React to user input
    if prompt := st.chat_input("What is up?"):
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})


        response = f"Ro Båt: {bot.chat(prompt)}"
        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(response)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})


def layout():
    st.title("Chatting with RO BÅT")
    chat()

    # if prompt := st.chat_input("Whazz up?"):
    #     with st.chat_message("assistant"):
    #         st.write(bot.chat(prompt))





if __name__ == "__main__":
    # print(read_data())
    layout()
