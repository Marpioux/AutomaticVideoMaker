from moviepy import VideoFileClip, TextClip, CompositeVideoClip, AudioFileClip

def creationMovie(subtitles, audio_path, output_path):
    # Charger la vidéo et l'audio
    video = VideoFileClip("./films/GameplayMinecraft.mp4")
    audio = AudioFileClip(audio_path)

    # Ajuster la durée de la vidéo à celle de l'audio
    video = video.with_duration(audio.duration).with_audio(audio)

    # Générer les clips de texte synchronisés
    text_clips = []
    for text, start, end in subtitles:
        txt_clip = TextClip(
            font="./font/Game Bubble.ttf",
            text=text,
            font_size=25,
            color="black",
        ).with_position("center").with_duration(end - start).with_start(start)
        
        text_clips.append(txt_clip)

    # Créer la vidéo finale avec le texte superposé
    final_video = CompositeVideoClip([video] + text_clips)

    # Exporter la vidéo finale
    final_video = final_video.with_audio(audio)
    final_video.write_videofile(output_path)
    return True