# AutomaticVideoMaker

AutomaticVideoMaker is a Python-based pipeline that automates the creation of videos with synchronized subtitles, audio, and text, and uploads them to TikTok. The project integrates various tools and APIs to generate stories, convert text to speech, synchronize audio with subtitles, and create videos.

## Features

- **Story Generation**: Uses OpenAI's GPT model to generate short stories.
- **Text-to-Speech Conversion**: Converts generated stories into audio using TTS.
- **Subtitle Synchronization**: Synchronizes subtitles with the generated audio using Vosk.
- **Video Creation**: Combines video, audio, and subtitles into a final video using MoviePy.
- **TikTok Upload**: Automatically uploads the generated video to TikTok via its API.

## Project Structure

```
.env                     # Environment variables (API keys, etc.)
.gitignore               # Git ignore file
entire_pipeline.py       # Main script to run the entire pipeline
films/                   # Directory for video files
font/                    # Directory for custom fonts
functions/               # Directory for core functions
    movieMakerTest.py    # Video creation logic
    storyGeneration.py   # Story generation logic
    synchronisationVoiceText.py # Subtitle synchronization logic
    textToSpeech.py      # Text-to-speech conversion logic
    upload.py            # TikTok upload logic
garbage/                 # Temporary or unused files
models/                  # Directory for Vosk model files
sounds/                  # Directory for audio files
```

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd AutomaticVideoMaker
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Download the Vosk model and place it in the `models/` directory.

4. Add your API keys to the `.env` file:
   ```
   OPENAI_API_KEY="your_openai_api_key"
   TIKTOK_ACCESS_TOKEN="your_tiktok_access_token"
   ```

## Usage

Run the main pipeline script to generate and upload a video:
```bash
python entire_pipeline.py
```

### Pipeline Steps

1. **Story Generation**: Generates a short story using OpenAI's GPT model.
2. **Text-to-Speech**: Converts the story into an audio file.
3. **Subtitle Synchronization**: Synchronizes subtitles with the audio.
4. **Video Creation**: Combines the audio, subtitles, and a base video into a final video.
5. **TikTok Upload**: Uploads the video to TikTok.

## Dependencies

- Python 3.10+
- [MoviePy](https://zulko.github.io/moviepy/)
- [Vosk](https://alphacephei.com/vosk/)
- [TTS](https://github.com/coqui-ai/TTS)
- [Requests](https://docs.python-requests.org/en/latest/)
- [dotenv](https://pypi.org/project/python-dotenv/)

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests.