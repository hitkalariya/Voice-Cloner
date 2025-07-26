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
    for code, lang in SUPPORTED_LANGS.items():
        if lang.lower() == lang_name.lower():
            return code
    return "en" 