import os
from datetime import datetime

def generate_audio_id(indentation: int = 0) -> str:
    """
    Generate a unique audio ID based on the current date and an indentation value.
    Checks for existing files in ../sounds/generate and increments the indentation if necessary.
    """
    current_date = datetime.now().strftime("%Y%m%d")
    base_path = "../sounds/generate"
    os.makedirs(base_path, exist_ok=True)  # Ensure the directory exists

    while True:
        audio_id = f"audio_{current_date}_{indentation:03d}"
        if not os.path.exists(os.path.join(base_path, f"{audio_id}.mp3")):
            return audio_id
        indentation += 1

def generate_video_id(indentation: int = 0) -> str:
    """
    Generate a unique video ID based on the current date and an indentation value.
    Checks for existing files in ../films/generate and increments the indentation if necessary.
    """
    current_date = datetime.now().strftime("%Y%m%d")
    base_path = "../films/generate"
    os.makedirs(base_path, exist_ok=True)  # Ensure the directory exists

    while True:
        video_id = f"video_{current_date}_{indentation:03d}"
        if not os.path.exists(os.path.join(base_path, f"{video_id}.mp4")):
            return video_id
        indentation += 1

print(generate_audio_id())
print(generate_video_id())