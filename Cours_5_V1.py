import streamlit as st
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Configuration page
st.set_page_config(page_title="Assistant Collège", page_icon="📚")

st.title("📚 Assistant Scolaire - Collège")
st.write("Pose-moi une question (maths, français, histoire, sciences...)")

# Initialiser l'historique
if "messages" not in st.session_state:
    st.session_state.messages = []

# Afficher l'historique
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Configuration du modèle Mistral
llm = ChatMistralAI(
    model="mistral-large-latest",
    temperature=0.4,  # api_key="Rentrez votre clée API."
    api_key="FLxc9HxvjxOVcYNozF8CP4oPzDZvcaoT",
)

# Prompt pédagogique
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
Tu es un assistant pédagogique pour des élèves de collège (11-15 ans).

Règles importantes :
- Explique simplement.
- Utilise des exemples concrets.
- Fais des phrases courtes.
- Sois bienveillant et encourageant.
- Si la question est compliquée, découpe en étapes.
- Ne donne jamais de contenu inapproprié pour des mineurs.
            """,
        ),
        ("human", "{question}"),
    ]
)

chain = prompt | llm | StrOutputParser()

# Zone de saisie utilisateur
if user_input := st.chat_input("Ta question ici..."):

    # Afficher message utilisateur
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Générer réponse
    response = chain.invoke({"question": user_input})

    # Afficher réponse
    st.chat_message("assistant").markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
