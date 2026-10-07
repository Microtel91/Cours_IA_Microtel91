import streamlit as st

st.title("Exemple chat_input")

message = st.chat_input("Écris quelque chose...")

if message:
    st.write("Tu as écrit :", message)
