FRIDAY-2 Digital Assistant

FRIDAY-2 is a small Python project that acts as a voice-activated personal assistant.
It listens when you call “Friday” and can help you with handy tasks like opening websites, playing music, reading news, or answering questions using OpenAI GPT.

Features
Wake Word

Say “Friday” to get its attention.

Open Websites

Quick commands like:
open google, open youtube, open facebook, open linkedin.

Play Music

Plays songs from your musicLibrary.py directly.

If a song isn’t in your library, it searches YouTube and plays the first result automatically.

Read News

Fetches top headlines using NewsAPI.

Chat / Answer Questions

If FRIDAY-2 doesn’t understand a command, it queries GPT for a short answer.

Speech

Speaks back using gTTS + pygame, with pyttsx3 as a backup.

Project Structure
FRIDAY-2-digital-assistant/
│
├── main.py          # main logic of the assistant
├── musicLibrary.py  # your playlist (song names → YouTube links)
├── requirements.txt # Python dependencies
└── README.md        # project description

How to Use

Install dependencies:

pip install -r requirements.txt


Run the assistant:

python main.py


Say “Friday” followed by your command.
