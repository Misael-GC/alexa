import speech_recognition as sr
import pyttsx3, pywhatkit, wikipedia, datetime, keyboard 
from pygame import mixer
# import pyautogui

name = "Alexa"
listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()
    

def listen():
    try:
        with sr.Microphone() as source:
            print("Escuchando ...")
            pc = listener.listen(source)
            rec = listener.recognize_google(pc, language="es")
            rec = rec.lower()
            if name in rec:
                rec =  rec.replace(name, '')
    except:
        pass
    return rec

def run_alexa():
    while True:
        rec = listen()
        if 'reproduce' in rec:
            music = rec.replace('reproduce', '')
            print("Reproduciendo " + music)
            talk("Reproduciendo " + music)
            pywhatkit.playonyt(music)
            # pyautogui.press('space')
        elif 'busca' in rec or 'wikipedia' in rec:
            search = rec.replace('busca', '')
            wikipedia.set_lang("es")
            wiki = wikipedia.summary(search, 1)
            print(search + ": " + wiki)
            talk(wiki)

if __name__ == '__main__':
    run_alexa()
