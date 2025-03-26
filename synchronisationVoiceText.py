import json
import wave
from vosk import Model, KaldiRecognizer
def synchronisationVoiceText(audio_path):
    # Charger le modèle Vosk
    model_path = "models/vosk-model-small-en-us-0.15"
    model = Model(model_path)

    # Charger l'audio
    # Exemple de chemin vers un fichier audio
    #audio_path = "./sounds/output.wav
    wf = wave.open(audio_path, "rb")

    # Initialiser la reconnaissance
    rec = KaldiRecognizer(model, wf.getframerate())
    rec.SetWords(True)  # Active les timestamps des mots

    # Lire et reconnaître l'audio
    results = []
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            results.append(json.loads(rec.Result()))

    results.append(json.loads(rec.FinalResult()))

    # Extraire les sous-titres en regroupant par intervalle de temps (ex: 2 secondes)
    subtitles = []
    current_text = ""
    start_time = None
    max_duration = 1  # Regrouper toutes les 2 secondes

    for res in results:
        if "result" in res:
            for word in res["result"]:
                if start_time is None:
                    start_time = word["start"]
                current_text += word["word"] + " "

                # Quand on atteint 2 secondes, on stocke le segment
                if word["end"] - start_time >= max_duration:
                    subtitles.append((current_text.strip(), start_time, word["end"]))
                    current_text = ""
                    start_time = None

    # Ajouter le dernier segment s'il reste du texte
    if current_text:
        subtitles.append((current_text.strip(), start_time, word["end"]))

    # Afficher les résultats
    for sub in subtitles:
        print(sub)
    return subtitles
