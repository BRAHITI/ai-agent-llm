import streamlit as st
from openai import OpenAI
import openai

import os
from dotenv import load_dotenv

# Charger la clé API
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="Agent IA", page_icon="🤖")
st.title("🤖 Agent IA avec OpenAI")

# Entrée utilisateur
user_input = st.text_input("Posez une question à l'agent :")

# Réponse si input
if user_input:
    try:
        with st.spinner("Réponse en cours..."):
            client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": user_input}
                ]
            )
            agent_reply = response.choices[0].message['content']
            st.success(agent_reply)
    except Exception as e:
        st.error(f"Erreur : {e}")
