import spacy

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
from nltk.corpus import wordnet

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

nlp = spacy.load("en_core_web_sm")

def preprocess_spacy(text):
    doc = nlp(text)

    tokens = []
    clean_tokens = []
    lemmas = []

    for token in doc:
        tokens.append(token.text)

        if not token.is_stop and not token.is_punct:
            clean_tokens.append(token.text.lower())
            lemmas.append(token.lemma_.lower())

    return {
        "tokens": tokens,
        "clean_tokens": clean_tokens,
        "lemmas": lemmas,
        "final_text": " ".join(lemmas)
    }

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

def preprocess_nltk(text):
    tokens = word_tokenize(text)

    stop_words = set(stopwords.words("english"))
    lemmatizer = WordNetLemmatizer()
    pos_tags = pos_tag(tokens)

    clean_tokens = []
    lemmas = []

    for word, tag in pos_tags:
        if word.lower() not in stop_words and word.isalpha():
            clean_tokens.append(word.lower())
            wn_tag = get_wordnet_pos(tag)
            lemma = lemmatizer.lemmatize(word.lower(), pos=wn_tag)
            lemmas.append(lemma)

    return {
        "tokens": tokens,
        "clean_tokens": clean_tokens,
        "lemmas": lemmas,
        "final_text": " ".join(lemmas)
    }

if __name__ == "__main__":

    text = "The children were playing with the toys happily.Do you know what are the toys they were playing with?"

    print("INPUT TEXT:", text)

    print("\nspaCy Results")
    spacy_result = preprocess_spacy(text)
    print("Tokens:", spacy_result["tokens"])
    print("Clean Tokens:", spacy_result["clean_tokens"])
    print("Lemmas:", spacy_result["lemmas"])

    print("\nNLTK Results")
    nltk_result = preprocess_nltk(text)
    print("Tokens:", nltk_result["tokens"])
    print("Clean Tokens:", nltk_result["clean_tokens"])
    print("Lemmas:", nltk_result["lemmas"])

    corpus = [
        spacy_result["final_text"],
        nltk_result["final_text"]
    ]

    print("\nBag of Words")
    bow = CountVectorizer()
    bow_matrix = bow.fit_transform(corpus)
    print("Vocabulary:", bow.get_feature_names_out())
    print("Matrix:\n", bow_matrix.toarray())

    print("\nTF-IDF")
    tfidf = TfidfVectorizer()
    tfidf_matrix = tfidf.fit_transform(corpus)
    print("Vocabulary:", tfidf.get_feature_names_out())
    print("Matrix:\n", tfidf_matrix.toarray())
