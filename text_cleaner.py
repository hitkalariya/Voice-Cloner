import re

def preprocess_text(text, lang="en"):
    """Clean and normalize input text for TTS processing."""
    text = text.strip()
    text = language_specific_clean(text, lang)
    return text.lower()

def language_specific_clean(text, lang):
    """Apply language-specific regex cleaning rules."""
    if lang == "en":
        text = re.sub(r"[^a-zA-Z0-9\s.,!?']", "", text)
    elif lang == "hi":
        text = re.sub(r"[^\u0900-\u097F\s.,!?']", " ", text)
    # Add more language rules here as needed
    return text

def text_statistics(text):
    """Return basic statistics about the input text."""
    return {
        "length": len(text),
        "num_words": len(text.split()),
        "num_unique": len(set(text.split())),
    } 