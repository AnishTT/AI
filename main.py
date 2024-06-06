import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
import subprocess
import datetime
import time


def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio, language='en-in')
            print(said)
        except Exception as e:
            print("Exception: " + str(e))
    return said.lower()


def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"

    with open(file_name, "w") as f:
        f.write(text)
        subprocess.Popen(["notepad.exe", file_name])


wake = "hello"
while True:
    text = get_audio()
    if text.count(wake) > 0:
        speak("hey how can I help you?")
        text = get_audio()

        NOTE_STR = ["make a note", "write this down", "remember this"]
        for phrase in NOTE_STR:
            if phrase in text:
                speak("what would you like me to add to your note?")
                note_text = get_audio()
                note(note_text)
                speak("I have made note of that")