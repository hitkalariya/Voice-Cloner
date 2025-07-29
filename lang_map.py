SUPPORTED_LANGS = {
    "sa": "Sanskrit",
    "en": "English",
    "hi": "Hindi",
    "bn": "Bengali",
    "ta": "Tamil",
    "te": "Telugu",
    "gu": "Gujarati",
    "ml": "Malayalam",
    "mr": "Marathi",
    "kn": "Kannada",
    "pa": "Punjabi",
    "or": "Odia",
    "as": "Assamese",
    "ur": "Urdu",
    "sd": "Sindhi",
}

def lookup_lang_code(lang_name):
    """Return the language code for a given language name (case-insensitive). Defaults to 'en'."""
    for code, lang in SUPPORTED_LANGS.items():
        if lang.lower() == lang_name.lower() or code.lower() == lang_name.lower():
            return code
    return "en"

def list_language_names():
    """Return a list of all supported language names."""
    return list(SUPPORTED_LANGS.values())

def is_supported_language(query):
    """Check if a language code or name is supported."""
    query = query.lower()
    return any(query == code.lower() or query == lang.lower() for code, lang in SUPPORTED_LANGS.items()) 