import os
import requests
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("HF_API_TOKEN")

API_URL = "https://router.huggingface.co/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

def chat_with_model():
    conversation = []
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break

        payload = {
            "model": "mistralai/Mistral-7B-Instruct-v0.2",
            "messages": conversation + [{"role": "user", "content": user_input}]
        }

        response = requests.post(API_URL, headers=headers, json=payload).json()
        assistant_message = response["choices"][0]["message"]["content"]

        print("Assistant:", assistant_message)

        # Add assistant reply to conversation history
        conversation.append({"role": "user", "content": user_input})
        conversation.append({"role": "assistant", "content": assistant_message})

chat_with_model()