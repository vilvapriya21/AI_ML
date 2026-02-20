import spacy

nlp = spacy.load("en_core_web_sm")

text = "The cats are running quickly."

doc = nlp(text)

clean_tokens = []

for token in doc:
    if not token.is_stop and not token.is_punct:
        clean_tokens.append(token.text.lower())

print("CLEAN TOKENS:", clean_tokens)
