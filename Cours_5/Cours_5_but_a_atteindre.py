import streamlit as st
from langchain_mistralai import ChatMistralAI

# Initialisation du modèle
llm = ChatMistralAI(
    model="mistral-large-latest", temperature=0, api_key="Rentrez votre clée API"
)

# Initialisation de l'historique dans la session Streamlit
if "history" not in st.session_state:
    st.session_state.history = [
        {
            "role": "system",
            "content": "Tu es un enseignant qui s'adresse à des enfants de 8 ans.",
        }
    ]

# Titre de l'application
st.title("🤖 Chatbot Enseignant (8 ans)")

# Affichage des messages précédents (sauf system)
for message in st.session_state.history:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Zone de saisie utilisateur
user_input = st.chat_input("Écris ton message ici...")

if user_input:
    # Ajouter le message utilisateur à l'historique
    st.session_state.history.append({"role": "user", "content": user_input})

    # Afficher le message utilisateur
    with st.chat_message("user"):
        st.markdown(user_input)

    # Appel au modèle
    response = llm.invoke(st.session_state.history)

    # Ajouter la réponse à l'historique
    st.session_state.history.append({"role": "assistant", "content": response.content})

    # Afficher la réponse
    with st.chat_message("assistant"):
        st.markdown(response.content)
