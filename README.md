# FRIDAY-2 Digital Assistant
FRIDAY-2 is a small Python project I built as a voice-activated personal assistant.
It listens when you call “Friday”, and can do a few handy things for you — open websites, play songs, read the news, and even answer your questions using OpenAI GPT.

What it can do

Wake word: Say “Friday” to get its attention.

Open sites: Quick commands like open google, open youtube, open facebook, open linkedin.

Play music:

If the song is in musicLibrary.py, it plays directly.

If not, it searches YouTube and starts the first result automatically.

Read news: Gets top headlines using NewsAPI.

Chat/answer: If it doesn’t understand, it asks GPT (short answers).

Speaks back: Uses gTTS + pygame (with pyttsx3 as backup).

Project structure
FRIDAY-2-digital-assistant-/
│
├── main.py          # main logic
├── musicLibrary.py  # your playlist (song names → YouTube links)
├── requirements.txt # dependencies
└── README.md

Setup

Clone the repo:

git clone https://github.com/PratyushKr31/FRIDAY-2-digital-assistant-.git
cd FRIDAY-2-digital-assistant-


Install dependencies:

pip install -r requirements.txt


If you don’t have requirements.txt, just run:

pip install speechrecognition pyttsx3 gTTS pygame requests openai pyaudio


Note: On Windows, pyaudio sometimes needs:

pip install pipwin
pipwin install pyaudio


Set your API keys (OpenAI + NewsAPI):

Windows (PowerShell):

setx OPENAI_API_KEY "your-openai-key"
setx NEWSAPI_KEY "your-newsapi-key"


Linux/Mac:

export OPENAI_API_KEY="your-openai-key"
export NEWSAPI_KEY="your-newsapi-key"

Run it
python main.py


Say Friday, then try things like:

open google

play hello

play blinding lights (not in playlist → goes to YouTube)

news

what is python?

Future improvements

Add Spotify or other music sources.

Continuous listening mode.

Simple GUI so you don’t need the terminal.
