from TTS.api import TTS

device = "cpu"
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)


# Conversion du texte en audio avec Caudi TTS
def text_to_speech(text, output_audio_path):
    tts.tts_to_file(
        text=text, 
        speaker="Craig Gutsy",  # Utilise un speaker par défaut
        language="en",  # Langue
        file_path=output_audio_path
    )
    print(f"🔊 Audio enregistré sous : {output_audio_path}")
    return output_audio_path