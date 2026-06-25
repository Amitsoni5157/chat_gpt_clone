import streamlit as st

def main():
    st.set_page_config(
        page_title="Your own ChatGpt",
        page_icon="🤖"
    )

    st.header("Your own ChatGpt 🤖")

    with st.sidebar:
        user_input = st.text_input("Your message: ", key="user_input")

if __name__ == '__main__':
    main()