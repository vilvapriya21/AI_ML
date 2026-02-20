import requests

url = "http://localhost:11434/api/generate"

# TECHNIQUE 1: System Role (Controls AI behavior)
prompt = """
SYSTEM: You are a professional Python code reviewer. 
Be strict, short, and give only improvements.

USER: Review this code:
x = []
for i in range(10):
    x.append(i*2)
"""

# # TECHNIQUE 2: Few-Shot (Give examples to guide AI)
# prompt = """
# Classify sentiment. Examples:
# "I love this" -> Positive
# "This is bad" -> Negative
# "It is okay"  -> Neutral

# Now classify: "The product works fine"
# """

# # TECHNIQUE 3: Chain of Thought (Force step-by-step thinking)
# prompt = """
# Solve this step by step:
# A server handles 100 requests/min. 
# If traffic grows 30% each hour, 
# how many requests after 3 hours?
#"""

payload = {
    "model": "mistral",
    "prompt": prompt,
    "temperature": 0.3,
    "num_predict": 300,
    "stream": False
}

r = requests.post(url, json=payload)
print(r.json()["response"])