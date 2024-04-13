import streamlit as st
from streamlit_chat import message
from dotenv import load_dotenv
import os
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate

llm = Ollama(model="phi:latest", base_url="http://ollama-container:11434", verbose=True)

def sendPrompt(prompt):
    global llm
    response = llm.invoke(prompt)
    return response

st.title("Chat with AI")

#instruction = PromptTemplate.from_template("Yor are very good AI companion. Your responsibility is to help Human with the emotional support. Act as emotional parter and reply accordingly")

mode = st.selectbox("Choose AI mode", ("AI Companion", "AI Assistant"))

if mode == "AI Companion":
    instruction = "Hi, I'm your AI companion. How can I support you today?"
else:
    instruction = "Hi, I'm your AI assistant. How can I assist you today?"

if "messages" not in st.session_state.keys():
    st.session_state.messages = [
        {"role": "assistant", "content": instruction}
    ]

if prompt := st.chat_input("Your Question"):
    st.session_state.messages.append({"role": "user", "content": prompt})

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("thinking..."):
            response = sendPrompt(["Yor are very good AI companion. Your responsibility is to help Human with the emotional support. Act as emotional parter and reply accordingly"] + st.session_state.messages)
            print(response)
            st.write(response)
            message = {"role": "assistant", "content": response}
            st.session_state.messages.append(message)