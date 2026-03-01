import streamlit as st

st.title("Exemple historique")

if "history" not in st.session_state:
    st.session_state.history = []

message = st.chat_input("Écris un message")

if message:
    st.session_state.history.append(message)

for msg in st.session_state.history:
    st.write(msg)
