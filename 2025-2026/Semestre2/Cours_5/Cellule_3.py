import streamlit as st

st.title("Exemple session_state")

# Initialisation
if "compteur" not in st.session_state:
    st.session_state.compteur = 0

# Bouton pour modifier la valeur
if st.button("Incrémenter"):
    st.session_state.compteur += 1

st.write("Valeur actuelle :", st.session_state.compteur)
