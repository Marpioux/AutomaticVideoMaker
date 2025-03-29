import os
import requests
from dotenv import load_dotenv

# Charger les variables d’environnement
load_dotenv()

# Récupérer la clé API
TIKTOK_ACCESS_TOKEN = os.getenv("TIKTOK_ACCESS_TOKEN")


def upload_to_tiktok(video_path, privacy="public"):
    """
    Upload une vidéo sur TikTok avec une option de confidentialité.

    :param video_path: Chemin du fichier vidéo
    :param privacy: "public" pour tout le monde ou "private" pour soi-même uniquement
    """
    # Vérifier le niveau de confidentialité
    privacy_level = "PUBLIC_TO_EVERYONE" if privacy == "public" else "SELF_ONLY"

    # Étape 1: Initialiser la publication
    init_url = "https://open.tiktokapis.com/v2/post/publish/video/init/"
    headers = {
        "Authorization": f"Bearer {TIKTOK_ACCESS_TOKEN}",
        "Content-Type": "application/json; charset=UTF-8",
    }
    data = {
        "post_info": {
            "title": "Vidéo test #API",
            "privacy_level": privacy_level,
            "disable_duet": False,
            "disable_comment": False,
            "disable_stitch": False
        },
        "source_info": {
            "source": "FILE_UPLOAD",
            "video_size": os.path.getsize(video_path)
        }
    }

    response = requests.post(init_url, headers=headers, json=data)
    
    if response.status_code != 200:
        print("❌ Erreur lors de l'initialisation :", response.json())
        return
    
    response_data = response.json().get("data", {})
    upload_url = response_data.get("upload_url")
    publish_id = response_data.get("publish_id")

    if not upload_url:
        print("❌ Impossible d'obtenir l'URL de téléchargement.")
        return

    # Étape 2: Envoyer la vidéo au serveur TikTok
    with open(video_path, "rb") as video_file:
        upload_response = requests.put(upload_url, headers={"Content-Type": "video/mp4"}, data=video_file)

    if upload_response.status_code == 200:
        print(f"✅ Vidéo envoyée avec succès ! (ID: {publish_id})")
    else:
        print("❌ Erreur lors de l'upload :", upload_response.text)


# Exemple d'utilisation :
upload_to_tiktok("C:\Users\marius.pingaud\OneDrive - BERGER-LEVRAULT\Bureau\perso\workflow_test\\films\generate\\video_20250329_002.mp4", privacy="private")  # Change "private" en "public" si besoin
