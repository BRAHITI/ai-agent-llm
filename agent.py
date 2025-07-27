# agent.py

import requests
import os
from dotenv import load_dotenv
load_dotenv()


def ask_openrouter(prompt):
    api_key = os.getenv("OPENROUTER_API_KEY")
    headers = {
        "Authorization": f"Bearer {api_key}",
        "HTTP-Referer": "https://ai-agent-llm-ryfb378tiv8qw7fhb36vrv.streamlit.app/",  # remplace par ton app Streamlit publique si tu en as une
        "Content-Type": "application/json"
    }

    body = {
        "model": "mistralai/mistral-7b-instruct",  # ou un autre modèle disponible
        "messages": [{"role": "user", "content": prompt}],
    }

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers=headers,
        json=body,
    )

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Erreur : {response.status_code} - {response.text}"

