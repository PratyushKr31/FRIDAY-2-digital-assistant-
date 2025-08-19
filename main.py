import speech_recognition as sr
import pyttsx3
import webbrowser
import musicLibrary
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os
import uuid


_tts_engine = pyttsx3.init()





def speak(text: str) -> None:   # speak the given text
    if not text:
        return
    try:
        tmp_path = f"temp_{uuid.uuid4().hex}.mp3"
        tts = gTTS(text)
        tts.save(tmp_path)

        pygame.mixer.init()
        pygame.mixer.music.load(tmp_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        pygame.mixer.music.unload()
        pygame.mixer.quit()
        os.remove(tmp_path)
    except Exception as e:
        print(f"[speak fallback]: {e}")
        try:
            _tts_engine.say(text)
            _tts_engine.runAndWait()
        except Exception as inner:
            print(f"[speak final fallback]: {inner}")
            print(f"[FRIDAY says]: {text}")



def aiProcess(command):
    client = OpenAI(api_key= os.getenv("OPENAI_API_KEY"))
    print(client.models.list())

    completion = client.chat.completions.create(
        model="gpt-5",
        messages=[
            {"role": "system", "content": "You are a virtual assistant named FRIDAY skilled in general tasks like Alexa and Google Cloud.Give short responses"},
            {"role": "user", "content": command}
            ])
    return completion.choices[0].message.content

def processcommand(c):      # process the provided command
        if "open google" in c.lower():
            webbrowser.open("https://www.google.com")
        elif "open facebook" in c.lower():
            webbrowser.open("https://facebook.com")
        elif "open youtube" in c.lower():
            webbrowser.open("https://youtube.com")
        elif "open linkedin" in c.lower():
            webbrowser.open("https://linkedin.com")      
        elif c.lower().startswith("play"):
            song= c.lower().split(" ",1)[1]                        #convert song name(lower case) in a list form and play everything after paly avoiding play word ("play hello" only select hello)
             # search ignoring case
            matches = [k for k in musicLibrary.music if k.lower() == song.lower()]
            if matches:
                link = musicLibrary.music[matches[0]]
                webbrowser.open(link)
                speak(f"Playing {matches[0]}")     
                webbrowser.open(link)
            else:
                print(song + "not in playist")

        elif "news" in c.lower():
            r=requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=3{newsapi}")
            if r.status_code == 200:
            # Parse the JSON response
             data = r.json()
            
            # Extract the articles
            articles = data.get('articles', [])
            
            # Print the headlines
            for article in articles:
                speak(article['title'])
        else:
            #OPEN AI
            output = aiProcess(c)
            speak(output)




if __name__== "__main__":
    speak("Initializing Friday. Say 'Friday' to activate me.")
    r= sr.Recognizer()
    while True:
        #listen for wake word 'friday"
        #obtain audio from the microphone
        
        try :
            with sr.Microphone()  as source:
                print("Say something!")
                # Adjust for ambient noise
                r.adjust_for_ambient_noise(source)
                # Listen to audio
                audio = r.listen(source,timeout=6,phrase_time_limit=10)
                call = r.recognize_google(audio)
                if(call.lower() == "friday"):      #checking for wake call
                  speak("yes. how can i help you")
                  # waiting for command
                  with sr.Microphone () as source:
                      print("Friday activate....")
                      # Adjust for ambient noise
                      r.adjust_for_ambient_noise(source)
                      # Listen to audio
                      audio = r.listen(source)
                      command = r.recognize_google(audio)
                      print(f"Command heard: {command}")
                      processcommand(command)
                      break
                      


        except sr.WaitTimeoutError:
            print("Error: Listening timed out while waiting for phrase to start")
        except sr.UnknownValueError:
            print("Error: Could not understand the audio")
        except sr.RequestError as e:
            print(f"Error: Could not request results from Google Speech Recognition; {e}")
        except Exception as e:
            print(f"Unexpected error: {type(e).__name__}: {e}")
