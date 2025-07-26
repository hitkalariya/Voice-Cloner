import re

def preprocess_text(text, lang="en"):
    text = text.strip()
    if lang == "en":
        text = re.sub(r"[^a-zA-Z0-9\s.,!?']", "", text)
    elif lang == "hi":
        text = re.sub(r"[^\u0900-\u097F\s.,!?']", " ", text)
    return text.lower() 