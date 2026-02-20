import requests

url = "http://localhost:11434/api/chat"  # NOTE: /api/chat not /api/generate

conversation_history = []

def chat(user_message):
    conversation_history.append({
        "role": "user",
        "content": user_message
    })
    
    payload = {
        "model": "mistral",
        "messages": conversation_history,  # full history = memory!
        "stream": False,
        "options": {"temperature": 0.7}
    }
    
    r = requests.post(url, json=payload)
    ai_reply = r.json()["message"]["content"]
    
    conversation_history.append({
        "role": "assistant",
        "content": ai_reply
    })
    
    return ai_reply

# System role - give AI a personality
conversation_history.append({
    "role": "system",
    "content": "You are a helpful Python tutor. Keep answers short and beginner friendly."
})

# Test it
print(chat("What is a list in Python?"))
print(chat("Give me an example of what you just explained"))  # remembers context!
print(chat("Now show me a dictionary"))