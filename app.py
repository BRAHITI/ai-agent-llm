import streamlit as st
from agent import ask_openrouter 

st.title("Agent IA - Ma première application via l'IA opensource OpenRouter")


question = st.text_input("Posez votre question, je suis là pour vous répondre :")

if st.button("Envoyer") and question:
    response = ask_openrouter(question)
    st.write("Réponse de l'IA :")
    st.write(response)
