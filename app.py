import streamlit as st
from agent import ask_openrouter 

st.title("Ma première application IA ")


question = st.text_input("Bonjour M. Chef GRADEL, Posez votre question, je suis là pour vous répondre :")

if st.button("Envoyer") and question:
    response = ask_openrouter(question)
    st.write("Réponse de l'agent IA est résumé ci-dessous :")
    st.write(response)
