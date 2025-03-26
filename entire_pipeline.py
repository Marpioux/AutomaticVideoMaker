import openai
import requests
import json
import base64
import os
from TTS.api import TTS
"from moviepy.editor import *"

device = "cpu"
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

# Configuration des clés d’API
OPENAI_API_KEY = "<insert key>"
TIKTOK_ACCESS_TOKEN = "YOUR_TIKTOK_ACCESS_TOKEN"

# Génération de l’histoire avec GPT-3.5
def generate_story():
    client = openai.OpenAI(api_key=OPENAI_API_KEY)
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a storytelling assistant."},
            {"role": "user", "content": "Write a short 200-word story about a magical adventure."}
        ],
        max_tokens=200
    )

    return response.choices[0].message.content 

# Conversion du texte en audio avec Google TTS
def text_to_speech(text, output_audio_path="./paul.mp3"):
    tts.tts_to_file(
        text=text, 
        speaker="Craig Gutsy",  # Utilise un speaker par défaut
        language="en",  # Langue
        file_path=output_audio_path
    )
    print(f"🔊 Audio enregistré sous : {output_audio_path}")
    return output_audio_path

# Création de la vidéo avec l'audio et une image de fond
def create_video(image_path="background.jpg", audio_path="output.mp3", output_video="output.mp4"):
    image_clip = ImageClip(image_path, duration=AudioFileClip(audio_path).duration)
    audio_clip = AudioFileClip(audio_path)

    video = image_clip.set_audio(audio_clip)
    video.write_videofile(output_video, fps=24, codec="libx264", audio_codec="aac")
    print("🎬 Vidéo créée :", output_video)
    return output_video

# Publication sur TikTok via l’API
def upload_to_tiktok(video_path):
    url = "https://open-api.tiktok.com/share/video/upload"
    headers = {"Authorization": f"Bearer {TIKTOK_ACCESS_TOKEN}"}
    files = {"video": open(video_path, "rb")}

    response = requests.post(url, headers=headers, files=files)
    
    if response.status_code == 200:
        print("✅ Vidéo publiée avec succès sur TikTok !")
    else:
        print("❌ Erreur lors de la publication :", response.text)

# Exécution du workflow
text_to_speech("example pour paul mon super pote")
"""story_text = generate_story()
print("📜 Histoire générée :", story_text)
audio_file = text_to_speech(story_text)"""
"""video_file = create_video()
upload_to_tiktok(video_file)"""
