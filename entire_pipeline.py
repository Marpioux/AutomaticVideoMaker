from functions.storyGeneration import generate_story
from functions.textToSpeech import text_to_speech
from functions.synchronisationVoiceText import synchronisationVoiceText
from functions.movieMakerTest import creationMovie
from functions.upload import upload_to_tiktok

# Generer les IDs du jour pour vidéos et sons
# ToDo

# Génération de l’histoire avec GPT-3.5
story = generate_story()

# Conversion du texte en audio avec Caudi TTS
convertion = text_to_speech(story, "./sounds/output.wav")

# Création des sous-titres avec synchronisation
subtitles = synchronisationVoiceText("./sounds/output.wav")

# Verification textuel des sous-titres
# ToDo

# Création de la vidéo avec MoviePy
movie = creationMovie(subtitles, "./sounds/output.wav", "./films/output.mp4")

# Publication sur TikTok via l’API
upload_to_tiktok("./films/output.mp4")