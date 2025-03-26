from moviepy import VideoFileClip, TextClip, CompositeVideoClip, AudioFileClip
from synchronisationVoiceText import synchronisationVoiceText  # Fonction qui extrait les sous-titres

# 🟢 Étape 1 : Charger la vidéo et l'audio
video = VideoFileClip("./films/GameplayMinecraft.mp4")  # Vidéo complète
audio = AudioFileClip("./sounds/output.wav")  # Audio complet

# Ajuster la durée de la vidéo à celle de l'audio
video = video.with_duration(audio.duration).with_audio(audio)

# 🔵 Étape 2 : Extraire les sous-titres avec les bons timings
subtitles = synchronisationVoiceText("./sounds/output.wav")

# 🔴 Étape 3 : Générer les clips de texte synchronisés
text_clips = []
for text, start, end in subtitles:
    txt_clip = TextClip(
        font="./font/Game Bubble.ttf",
        text=text,
        font_size=25,
        color="black",
        #bg_color="black",
    ).with_position("center").with_duration(end - start).with_start(start)
    
    text_clips.append(txt_clip)

# 🟠 Étape 4 : Créer la vidéo finale avec le texte superposé
final_video = CompositeVideoClip([video] + text_clips)

# 🟣 Étape 5 : Exporter la vidéo finale
final_video = final_video.with_audio(audio)
final_video.write_videofile("FirstCompleteTest.mp4")
