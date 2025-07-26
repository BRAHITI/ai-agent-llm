# 🧠 Agent IA avec LLMs (OpenAI)

Ce projet est un **agent intelligent** qui utilise les **modèles de langage (LLMs)** d'OpenAI pour répondre à des questions depuis un terminal.  
Il est écrit en Python et fonctionne dans un environnement virtuel.

---

## 🚀 Fonctionnalités

- Utilise l'API OpenAI (ChatGPT)
- Interactions en ligne de commande
- Utilisation sécurisée via `.env` (clé API)
- Facile à étendre (Streamlit, mémoire, LangChain...)

---

## 📦 Installation

### 1. Cloner le projet

```bash
git clone https://github.com/ton-utilisateur/ai-agent-llm.git
cd ai-agent-llm






### 2. Créer et activer un environnement virtuel

python -m venv llm_env
source llm_env/bin/activate     # Windows : llm_env\Scripts\activate


### 3. Installer les dépendances

pip install -r requirements.txt



🔐 Configuration

1. Crée un fichier .env à la racine du projet :

OPENAI_API_KEY=sk-ta_cle_api_ici

2. Ajoute .env à .gitignore pour protéger ta clé.


🧪 Utilisation

python agent.py


📁 Structure du projet

ai-agent-llm/
├── agent.py            # Script principal
├── .env                # Contient la clé API (non partagé)
├── .gitignore
├── requirements.txt    # Dépendances
└── README.md           # Ce fichier