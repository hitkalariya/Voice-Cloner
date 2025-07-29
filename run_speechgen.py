import os
import torch
from audio_synth_core import initialize_models, generate_audio
from lang_map import SUPPORTED_LANGS, lookup_lang_code

def export_audio(waveform, path):
    """Save the generated audio waveform to a file."""
    torch.save(waveform, path)

def list_languages():
    print("\nSupported Languages:")
    for code, lang in SUPPORTED_LANGS.items():
        print(f"  {code}: {lang}")

def cli_entry():
    print("""
====================================
  PolyVoice Synthesizer CLI
  Multilingual Speech & Voice Cloning
  Project: https://github.com/hitkalariya
====================================
""")
    list_languages()

    t2_model, wg_model = initialize_models()
    print("\nModels loaded. Ready to synthesize speech!")

    user_text = input("\nEnter the text to synthesize: ")
    lang_input = input("Enter language (name or code): ")
    lang_code = lookup_lang_code(lang_input)

    custom_filename = input("Enter output filename (leave blank for default): ").strip()
    if not custom_filename:
        custom_filename = "output_voice.wav"
    out_file = os.path.join("data", "synthesized_audio", custom_filename)
    os.makedirs(os.path.dirname(out_file), exist_ok=True)

    print(f"\nSynthesizing speech in '{SUPPORTED_LANGS.get(lang_code, lang_code)}'...")
    audio_wave = generate_audio(user_text, t2_model, wg_model, lang=lang_code)
    export_audio(audio_wave, out_file)

    print(f"\nSpeech file created at: {out_file}\n")
    print("Thank you for using PolyVoice Synthesizer!")

if __name__ == "__main__":
    cli_entry() 