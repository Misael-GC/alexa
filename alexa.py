import speech_recognition as sr
import pyttsx3, pywhatkit, wikipedia, datetime, keyboard
from pygame import mixer
# import pyautogui

# Definición del nombre del asistente
name = "Alexa"
listener = sr.Recognizer() # Inicialización del reconocedor de voz
engine = pyttsx3.init()

# Obtención de las voces disponibles y selección de la primera voz
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


# Función para que el asistente hable
def talk(text):
    engine.say(text)
    engine.runAndWait()
    
# Función para escuchar y reconocer el habl
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

# Función principal del asistente
def run_alexa():
    while True:
        rec = listen()
        if 'reproduce' in rec:
            music = rec.replace('reproduce', '')
            print("Reproduciendo " + music)
            talk("Reproduciendo " + music)
            pywhatkit.playonyt(music) # Busca y reproduce la canción en YouTube
            # pyautogui.press('space')
        elif 'busca' in rec or 'wikipedia' in rec:
            search = rec.replace('busca', '')
            wikipedia.set_lang("es")
            wiki = wikipedia.summary(search, 1)
            print(search + ": " + wiki)
            talk(wiki)
        elif 'alarma' in rec:
            num = rec.replace('alarma', '')
            num = num.strip()
            talk("Alarma activada a las " + num + " horas")
            while True:
                if datetime.datetime.now().strftime('%H:%M') == num:
                    print("DESPIERTA!!!")
                    talk("¿Es hora de despertar!")
                    mixer.init()
                    mixer.music.load("auronplay-alarma.mp3")
                    mixer.music.play()
                    if keyboard.read_key() == "s":
                        mixer.music.stop()
                    break
                    

if __name__ == '__main__':
    run_alexa()
