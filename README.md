# FRIDAY-2: Voice-Activated Digital Assistant

**FRIDAY-2** is a Python-based, voice-activated personal assistant that listens to your commands and helps you perform tasks like opening websites, playing music, fetching news, and more. Think of it as your very own AI companion!

---

## Features

* **Wake Word Activation**: Just say **“Friday”** to start interacting.
* **Open Websites**: Quick commands like:

  * “Open Google”
  * “Open YouTube”
  * “Open LinkedIn”
* **Play Music**:

  * Plays songs from a predefined music library (`musicLibrary.py`)
  * Can search YouTube if a song is not available locally
* **News Updates**: Fetches top headlines using the NewsAPI
* **Chat with GPT**: If a command is unknown, FRIDAY-2 uses OpenAI GPT to answer questions
* **Voice Feedback**: Provides spoken responses to your commands

---

## Repository Structure

```
FRIDAY-2-digital-assistant/
│
├─ main.py            # Core assistant logic & command handling
├─ musicLibrary.py    # Local music library
├─ README.md          # Project overview & setup instructions
├─ requirements.txt   # Python dependencies
└─ config.py          # API keys & constants (optional)
```

---

## Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/PratyushKr31/FRIDAY-2-digital-assistant-
```

2. **Navigate to the project folder**

```bash
cd FRIDAY-2-digital-assistant-
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Set up environment variables**

   * Create an `.env` file or use system environment variables for:

     ```
     OPENAI_API_KEY=<your_openai_api_key>
     NEWS_API_KEY=<your_news_api_key>
     ```

5. **Run the assistant**

```bash
python main.py
```

---

## How to Use

1. Say **“Friday”** to wake the assistant.
2. Speak your command clearly. Examples:

   * “Open YouTube”
   * “Play Believer by Imagine Dragons”
   * “Tell me the news”
3. FRIDAY-2 will respond with voice feedback.

---

## Future Enhancements

* Weather updates, reminders, and jokes
* GUI interface for visual feedback
* Music playlists and Spotify integration
* Custom wake word
* Memory-based GPT conversations

---

## Dependencies

* `speech_recognition` – Voice recognition
* `pyttsx3` – Text-to-speech
* `requests` – API requests
* `openai` – GPT chat integration
* `webbrowser` – Opening websites
* `youtube_search` – Searching YouTube

Install all dependencies via:

```bash
pip install -r
1.speechrecognition
2. pyaudio
3.setuptools
4.uuid
5.pyttsx3
6.requests
7.openai




---

## License

MIT License © 2025 Pratyush Kumar
  ![MIT License](https://img.shields.io/badge/license-MIT-green)
