import openai
import os
from dotenv import load_dotenv

# Charger les variables d’environnement
load_dotenv()

# Récupérer la clé API
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def generate_story():
    client = openai.OpenAI(api_key=OPENAI_API_KEY)
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a storytelling assistant."},
            {"role": "user", "content": "Tell me all you know about JFK death in 100 words"}
        ],
        max_tokens=200
    )

    return response.choices[0].message.content

# Exemple d'utilisation
story = generate_story()
print(story)
