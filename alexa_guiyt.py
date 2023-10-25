import speech_recognition as sr
import subprocess as sub
import pyttsx3, pywhatkit, wikipedia, datetime, keyboard, os
from tkinter import *
from PIL import Image, ImageTk
from pygame import mixer
# import pyautogui
# import threading as tr

main_window =Tk()
main_window.title("Alexa AI")


main_window.geometry("800x400")
main_window.wm_resizable(0,0) # este lo puedes descomentar, es para maximimizar la pantalla
main_window.configure(bg='#0F2027')

label_title = Label(main_window, text="Alexa AI", bg="#2C5364", fg="#bdc3c7", font=('Arial', 30, 'bold'))
label_title.pack(pady=10)

alexa_photo = ImageTk.PhotoImage(Image.open("alexa_photo.jpg"))
window_photo = Label(main_window, image=alexa_photo )
window_photo.pack(pady=10)

def mexican_voice():
    change_voice(0)
def english_voice():
    change_voice(1)
def spanish_voice():
    change_voice(2)

def change_voice(id):
    engine.setProperty('voice', voices[id].id)
    engine.setProperty('rate', 145)
    talk("Hola soy Alexa")


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

programs = {
    'word': r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE",
    'excel': r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE",
    'powerpoint': r"C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE",
    # 'programa': r"ruta puede ser zoom, telegram, whatsApp",
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
            for app in programs:
                if app in rec:
                    talk(f'Abriendo {app}')
                    os.startfile(programs[app])
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

button_voice_mx = Button(main_window, text="Voz México", fg="white", bg="#2193b0", font=("Arial", 10, "bold"), command=mexican_voice)
button_voice_mx.place(x=625, y=80, width=100, height=30)

button_voice_es = Button(main_window, text="Voz LATAM", fg="white", bg="#4286f4", font=("Arial", 10, "bold"), command=spanish_voice)
button_voice_es.place(x=625, y=115, width=100, height=30)

button_voice_us = Button(main_window, text="Voz USA", fg="white", bg="#373B44", font=("Arial", 10, "bold") , command=english_voice)
button_voice_us.place(x=625, y=150, width=100, height=30)




main_window.mainloop()