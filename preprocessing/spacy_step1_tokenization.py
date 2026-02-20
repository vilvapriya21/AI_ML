import spacy

nlp = spacy.load("en_core_web_sm")

text = "The cats are running quickly."

doc = nlp(text)

print("TOKENS:")
for token in doc:
    print(token.text)
