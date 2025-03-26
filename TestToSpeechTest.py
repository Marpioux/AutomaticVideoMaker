from piper import PiperVoice

# Charger une voix (par ex. français)
voice = PiperVoice.load("fr_FR")

# Générer l'audio
text = "Bienvenue dans mon histoire magique."
audio = voice.synthesize(text)

# Sauvegarder l'audio
with open("output2.wav", "wb") as f:
    f.write(audio)
print("🔊 Fichier audio généré avec Piper TTS : output.wav")