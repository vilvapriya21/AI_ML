# import nltk
# from nltk.tokenize import word_tokenize
# from nltk.corpus import stopwords
# from nltk.stem import WordNetLemmatizer

# text = "The cats are running quickly."

# tokens = word_tokenize(text)

# stop_words = set(stopwords.words("english"))
# lemmatizer = WordNetLemmatizer()

# lemmas = [
#     lemmatizer.lemmatize(word.lower())
#     for word in tokens
#     if word.lower() not in stop_words and word.isalpha()
# ]

# print("LEMMAS:", lemmas)

import nltk
nltk.download('averaged_perceptron_tagger_eng')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')
# nltk.download('averaged_perceptron_tagger')

text = "The cats are running quickly."

tokens = word_tokenize(text)
stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

# Function to map NLTK POS tags to WordNet POS tags
def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN

# POS tagging
pos_tags = nltk.pos_tag(tokens)

# Lemmatization with POS
lemmas = [
    lemmatizer.lemmatize(word.lower(), get_wordnet_pos(tag))
    for word, tag in pos_tags
    if word.lower() not in stop_words and word.isalpha()
]

print("LEMMAS:", lemmas)
