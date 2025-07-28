import streamlit as st
from agent import ask_openrouter  # ou colle la fonction ici

st.title("Agent IA - via l'IA opensource OpenRouter")

question = st.text_input("Posez votre question à l'IA :")

if st.button("Envoyer") and question:
    response = ask_openrouter(question)
    st.write("Réponse de l'IA :")
    st.write(response)
