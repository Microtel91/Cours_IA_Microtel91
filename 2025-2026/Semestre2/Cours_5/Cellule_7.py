import streamlit as st

st.title("Exemple condition")

user_input = st.chat_input("Écris un message")

if user_input:
    st.success("Message reçu !")
    st.write(user_input)
else:
    st.info("En attente d'un message...")
