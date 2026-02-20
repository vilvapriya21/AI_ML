import spacy

nlp = spacy.load("en_core_web_sm")

text = "The cats are running quickly."

doc = nlp(text)

lemmas = []

for token in doc:
    if not token.is_stop and not token.is_punct:
        lemmas.append(token.lemma_.lower())

print("LEMMAS:", lemmas)
