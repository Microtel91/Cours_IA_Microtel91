import streamlit as st

st.title("Exemple chat_message")

with st.chat_message("user"):
    st.markdown("Bonjour !")

with st.chat_message("assistant"):
    st.markdown("Bonjour 😊 Comment puis-je t'aider ?")
