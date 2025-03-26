from moviepy import *

# Charger le fichier vidéo "GameplayMinecraft.mp4" et extraire une portion du clip entre 00:00:10 et 00:00:20
clip = VideoFileClip("GameplayMinecraft.mp4").subclipped(10, 20)

# Charger l'audio à ajouter (dans ce cas, "paul.mp3")
audio = AudioFileClip("paul.mp3")

# Créer un clip de texte avec un fond de texte, une couleur, une taille et une durée
txt_clip = TextClip(
    font="Game Bubble.ttf", text="Example pour paul", font_size=30, color="yellow"
)

# Positionner le texte au centre et définir la durée du texte
txt_clip = txt_clip.with_position("center").with_duration(10)

# Créer la vidéo composite en ajoutant le texte à la vidéo
final_video = CompositeVideoClip([clip, txt_clip])

# Assigner l'audio au clip final
final_video = final_video.with_audio(audio)

# Enregistrer le résultat dans un fichier vidéo
final_video.write_videofile("result.mp4")
