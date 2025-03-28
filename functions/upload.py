import os
import requests
from dotenv import load_dotenv

# Charger les variables d’environnement
load_dotenv()

# Récupérer la clé API
TIKTOK_ACCESS_TOKEN = os.getenv("TIKTOK_ACCESS_TOKEN")


def upload_to_tiktok(video_path):
    url = "https://open-api.tiktok.com/share/video/upload"
    headers = {"Authorization": f"Bearer {TIKTOK_ACCESS_TOKEN}"}
    files = {"video": open(video_path, "rb")}

    response = requests.post(url, headers=headers, files=files)
    
    if response.status_code == 200:
        print("✅ Vidéo publiée avec succès sur TikTok !")
    else:
        print("❌ Erreur lors de la publication :", response.text)