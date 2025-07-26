import os
import torch
from audio_synth_core import initialize_models, generate_audio
from lang_map import SUPPORTED_LANGS, lookup_lang_code

def export_audio(waveform, path):
    torch.save(waveform, path)

def cli_entry():
    print("SpeechGen - Multilingual Speech Synthesis")
    print("Available Languages:")
    for code, lang in SUPPORTED_LANGS.items():
        print(f"{code}: {lang}")

    t2_model, wg_model = initialize_models()

    user_text = input("Type the text you want to convert to speech: ")
    lang_input = input("Specify language (e.g., Hindi, Tamil, English, etc.): ")
    lang_code = lookup_lang_code(lang_input)

    audio_wave = generate_audio(user_text, t2_model, wg_model, lang=lang_code)
    out_file = "data/synthesized_audio/output_voice.wav"
    os.makedirs(os.path.dirname(out_file), exist_ok=True)
    export_audio(audio_wave, out_file)

    print(f"Speech file created at: {out_file}")

if __name__ == "__main__":
    cli_entry() 