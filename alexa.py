import speech_recognition as sr
import subprocess as sub
import pyttsx3, pywhatkit, wikipedia, datetime, keyboard, os
from pygame import mixer
# import pyautogui

# Definición del nombre del asistente
name = "Alexa"
listener = sr.Recognizer() # Inicialización del reconocedor de voz
engine = pyttsx3.init()

# Obtención de las voces disponibles y selección de la primera voz
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 145)

sites ={
    'google': 'https://www.google.com',
    'youtube': 'youtube.com',
    'facebook': 'facebook.com',
    'whatsapp': 'web.whatsapp.com',
    'servicios': 'misael-gc.github.io/Optima',
    'cursos': 'freecodecamp.org/learn'
}

files = {
    'carta': 'SED_Apuntes s2.pdf',
    'archivo': 'Nombre.pdf',
    'documento': 'Nombre.pdf',
}


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
        elif 'abre' in rec:
            for site in sites:
                if site in rec:
                    sub.call(f'start chrome.exe {sites[site]}', shell=True)
                    talk(f'Abriendo {site}')
        elif 'archivo' in rec:
            for file in files:
                if file in rec:
                    sub.Popen([files[file]], shell=True)
                    talk(f'Abriendo {file}')
        elif 'escribe' in rec:
            try:
                with open("nota.txt", 'a') as f:
                    write(f)
            except FileNotFoundError as e:
                file = open("nota.txt", 'w')
                write(file)
        elif 'termina' in rec:
            talk('Adios!!!')
            break

def write(f):
    talk("¿Qué quieres que escriba?")
    rec_write = listen()
    f.write(rec_write + os.linesep)
    f.close()
    talk("Listo, puedes revisarlo")
    sub.Popen("nota.txt", shell=True)




if __name__ == '__main__':
    run_alexa()
