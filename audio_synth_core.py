import torch
from text_cleaner import preprocess_text

def initialize_models():
    t2 = torch.hub.load("nvidia/DeepLearningExamples:torchhub", "nvidia_tacotron2")
    wg = torch.hub.load("nvidia/DeepLearningExamples:torchhub", "nvidia_waveglow")
    wg.eval()
    return t2, wg

def generate_audio(text, t2, wg, lang="en"):
    cleaned = preprocess_text(text, lang)
    seq = t2.text_to_sequence(cleaned, ["english_cleaner"])
    with torch.no_grad():
        mel, mel_post, _, _ = t2.infer(seq)
        audio = wg.infer(mel_post)
    return audio 