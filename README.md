# PolyVoice Synthesizer

PolyVoice Synthesizer is a Python tool for generating natural-sounding speech from text in multiple Indian languages. Powered by deep learning models, it enables both text-to-speech and simple voice mimicry, all from a user-friendly command-line interface.

---

## Features

- **Text-to-Speech (TTS):** Instantly convert text into speech audio in English and 14 Indian languages.
- **Voice Mimicry:** Basic voice cloning to produce speech with similar vocal characteristics.
- **Command-Line Simplicity:** Generate and save speech files with just a few prompts.

---

## Project Layout

```
PolyVoiceSynth/
├── data/
│   └── synthesized_audio/      # Output audio files
├── models/
│   ├── tacotron2/             # Tacotron 2 model files
│   └── waveglow/              # WaveGlow model files
├── run_speechgen.py           # Main CLI entry point
├── audio_synth_core.py        # Speech synthesis logic
├── text_cleaner.py            # Text preprocessing
├── lang_map.py                # Language code mapping
├── requirements.txt           # Dependencies
└── README_NEW.md              # This documentation
```

---

## Getting Started

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd PolyVoiceSynth
```

### 2. Set Up Your Environment
```bash
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```

### 3. Install Requirements
```bash
pip install -r requirements.txt
```

### 4. Run the Synthesizer
```bash
python run_speechgen.py
```

---

## How It Works

1. **Input:** Enter your text and select a language.
2. **Processing:** The system cleans the text and generates a mel spectrogram using Tacotron 2.
3. **Synthesis:** WaveGlow converts the spectrogram into a speech waveform.
4. **Output:** The audio is saved as a `.wav` file in `data/synthesized_audio/`.

---

## Supported Languages

- English
- Hindi
- Bengali
- Tamil
- Telugu
- Gujarati
- Malayalam
- Marathi
- Kannada
- Punjabi
- Odia
- Assamese
- Urdu
- Sindhi
- Sanskrit

---

## Roadmap

- [ ] Add a graphical user interface
- [ ] Enhance voice cloning with speaker embeddings
- [ ] Expand to more languages and models

---

## Contributing

Pull requests are welcome! Please fork the repo and submit your improvements.

---

## License

This project is open-source and available under the MIT License. 