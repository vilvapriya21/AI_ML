import requests

url = "http://localhost:11434/api/generate"

payload = {
    "model": "mistral",
    "prompt": "Explain overfitting in machine learning in simple terms.",
    "temperature": 1.7,
    "num_predict": 50,
    "stream": False
}

response = requests.post(url, json=payload)

print(response.json()["response"])