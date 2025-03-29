from functions.storyGeneration import generate_story
from functions.textToSpeech import text_to_speech
from functions.synchronisationVoiceText import synchronisationVoiceText
from functions.movieMakerTest import creationMovie
from functions.upload import upload_to_tiktok
from functions.idGeneration import generate_audio_id, generate_video_id
from functions.textVerification import modifier_subtitles

# Generer les IDs du jour pour vidéos et sons
audio_id = generate_audio_id()
video_id = generate_video_id()

# Génération de l’histoire avec GPT-3.5
story = generate_story()

# Conversion du texte en audio avec Caudi TTS
convertion = text_to_speech(story, f"./sounds/generate/{audio_id}.wav")

# Création des sous-titres avec synchronisation
subtitles = synchronisationVoiceText(f"./sounds/generate/{audio_id}.wav")

# Verification textuel des sous-titres
#subtitles = modifier_subtitles(story, subtitles)

# Création de la vidéo avec MoviePy
movie = creationMovie(subtitles, f"./sounds/generate/{audio_id}.wav", f"./films/generate/{video_id}.mp4")

# Publication sur TikTok via l’API
#upload_to_tiktok(f"./films/generate/{video_id}.mp4")