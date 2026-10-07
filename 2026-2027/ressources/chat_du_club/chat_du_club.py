"""Le chat du club : un petit harness autour d'un modèle, pour les élèves.

Lancer (invite Anaconda, depuis ce dossier) :
  set MISTRAL_API_KEY=la_cle_de_l_animateur      (Linux/Mac : export MISTRAL_API_KEY=...)
  streamlit run chat_du_club.py

La clé reste dans la variable d'environnement du poste : les élèves ne la voient jamais.
"""

import os

import requests
import streamlit as st

DOSSIER = os.path.dirname(os.path.abspath(__file__))
MISTRAL = "https://api.mistral.ai/v1/chat/completions"
OLLAMA = "http://localhost:11434/v1/chat/completions"

MODELES = {
    "Mistral Small (rapide)": (MISTRAL, "mistral-small-latest"),
    "Mistral Large (le plus fort)": (MISTRAL, "mistral-large-latest"),
    "Ministral 3B (tout petit)": (MISTRAL, "ministral-3b-latest"),
    "Qwen local (sans internet)": (OLLAMA, "qwen3.5:2b"),
}


with open(os.path.join(DOSSIER, "coach.txt"), encoding="utf-8") as f:
    COACH = f.read().strip()

MODES = {
    "Coach de projet": COACH,
    "Libre (presque sans consignes)": (
        "Tu parles à des enfants de 10 à 12 ans. Réponds en français. "
        "Ne demande jamais d'informations personnelles et refuse tout contenu inadapté à leur âge."
    ),
}


def appeler(url, modele, messages):
    entetes = {} if url == OLLAMA else {"Authorization": f"Bearer {os.environ.get('MISTRAL_API_KEY', '')}"}
    r = requests.post(url, headers=entetes, json={"model": modele, "messages": messages}, timeout=300)
    r.raise_for_status()
    return r.json()["choices"][0]["message"]["content"]


st.set_page_config(page_title="Chat du club", page_icon="🤖")
st.title("🤖 Le chat du club")

with st.sidebar:
    nom_modele = st.selectbox("Le modèle (le cerveau)", list(MODELES))
    mode = st.radio("Les consignes (le contexte)", list(MODES))
    if st.button("🧹 Nouvelle conversation"):
        st.session_state.historique = []
    st.caption("Rappel : je vérifie ce que dit l'IA, et je ne donne jamais d'informations personnelles.")

if "historique" not in st.session_state:
    st.session_state.historique = []

contexte = [{"role": "system", "content": MODES[mode]}] + st.session_state.historique

with st.expander("👀 Ce que le modèle va lire (son contexte)"):
    st.caption(f"{len(contexte)} messages, environ {sum(len(m['content']) for m in contexte) // 4} tokens. "
               "Tout ceci est renvoyé au modèle à CHAQUE question.")
    for m in contexte:
        st.markdown(f"**{m['role']}** : {m['content']}")

for m in st.session_state.historique:
    st.chat_message(m["role"]).markdown(m["content"])

if question := st.chat_input("Pose ta question…"):
    st.chat_message("user").markdown(question)
    st.session_state.historique.append({"role": "user", "content": question})
    url, modele = MODELES[nom_modele]
    with st.chat_message("assistant"), st.spinner("Le modèle écrit la suite…"):
        try:
            reponse = appeler(url, modele, [contexte[0]] + st.session_state.historique)
        except requests.RequestException as e:
            reponse = f"⚠️ Le modèle ne répond pas ({e.__class__.__name__}). Préviens l'animateur."
        st.markdown(reponse)
    st.session_state.historique.append({"role": "assistant", "content": reponse})
