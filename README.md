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

1. \*\*Clone the repository
