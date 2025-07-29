import torch
from text_cleaner import preprocess_text

def initialize_models():
    """Load Tacotron2 and WaveGlow models from torch.hub."""
    t2 = torch.hub.load("nvidia/DeepLearningExamples:torchhub", "nvidia_tacotron2")
    wg = torch.hub.load("nvidia/DeepLearningExamples:torchhub", "nvidia_waveglow")
    wg.eval()
    return t2, wg

def get_model_info():
    """Return a string describing the models used."""
    return (
        "Tacotron2: End-to-end text-to-speech model.\n"
        "WaveGlow: Neural vocoder for high-quality audio synthesis.\n"
        "(Both models from NVIDIA's DeepLearningExamples)"
    )

def generate_audio(text, t2, wg, lang="en", speaker_embedding=None):
    """
    Generate audio from text using Tacotron2 and WaveGlow.
    Optionally accepts a speaker_embedding for future voice cloning upgrades.
    """
    cleaned = preprocess_text(text, lang)
    seq = t2.text_to_sequence(cleaned, ["english_cleaner"])
    # Placeholder for speaker_embedding usage in future
    with torch.no_grad():
        mel, mel_post, _, _ = t2.infer(seq)
        audio = wg.infer(mel_post)
    return audio 