import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_agent(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",  # ou "gpt-3.5-turbo"
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message['content'].strip()

if __name__ == "__main__":
    while True:
        question = input("Vous: ")
        if question.lower() in ["exit", "quit"]:
            break
        print("Agent:", ask_agent(question))
