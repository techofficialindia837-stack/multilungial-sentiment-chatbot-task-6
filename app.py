import streamlit as st
from model import chatbot

st.set_page_config(page_title="Multilingual Chatbot")

st.title("🌍 Multilingual Sentiment Chatbot")

query = st.text_input("Enter your message:")

if st.button("Send"):
    if query:
        response, sentiment, lang = chatbot(query)

        st.write(f"🌐 Language: {lang}")
        st.write(f"🧠 Sentiment: {sentiment}")
        st.write("### 🤖 Response:")
        st.write(response)