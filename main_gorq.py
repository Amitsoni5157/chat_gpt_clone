import streamlit as st
from streamlit_chat import message
from dotenv import load_dotenv
import os

# It connects to groq server for using with llama model
from langchain_groq import ChatGroq
from langchain_core.messages import (
    SystemMessage,
    HumanMessage,
    AIMessage
)
# It will store only 10 messages for saving tokens
MAX_MESSAGES = 10

def init():
    load_dotenv()

    if not os.getenv("GROQ_API_KEY"):
        print("GROQ_API_KEY is not set")
        exit(1)
    else:
        print("GROQ_API_KEY is set") 
        
        # For showing on screen
        st.set_page_config(
            page_title="Your own ChatGpt",
            page_icon="🤖"
    )


def main():
    init()
    # It connects with gorq and temperature gives you perfact answe
    chat = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

    # for seving conversation in sesssion state
    if("messages" not in st.session_state):
        st.session_state.messages =[
            SystemMessage(content="You are helpful assistant.")
        ]

    st.header("Your own ChatGpt 🤖")

    with st.sidebar:
        user_input = st.chat_input("Type your message...", key="user_input")

    if user_input:
        # message(user_input,is_user=True)
        st.session_state.messages.append(HumanMessage(content=user_input))
        # So here er are not sending full chat we are just connecting first system messages with 10 previous chats
        with st.spinner("Thinking.... "):
            response = chat.invoke(
                # Storig in our session ai answer
    [st.session_state.messages[0]] + st.session_state.messages[-MAX_MESSAGES:]
)
            # response = chat(st.session_state.messages)
            
            st.session_state.messages.append(AIMessage(content=response.content))
        
            
# will show all the messages one by one
    messages = st.session_state.get('messages', [])
    for i, msg in enumerate(st.session_state.messages):
        if isinstance(msg, HumanMessage):
            message(msg.content, is_user=True, key=str(i) + '_user')
        elif isinstance(msg, AIMessage):
            message(msg.content, is_user=False, key=str(i) + '_ai')


if __name__ == '__main__':
    main()