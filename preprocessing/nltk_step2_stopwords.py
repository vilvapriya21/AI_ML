import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

text = "The cats are running quickly."

tokens = word_tokenize(text)

stop_words = set(stopwords.words("english"))

filtered = [word.lower() for word in tokens if word.lower() not in stop_words and word.isalpha()]

print("CLEAN TOKENS:", filtered)