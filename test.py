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


# Definición del nombre del asistente
name = "Alexa"
listener = sr.Recognizer() # Inicialización del reconocedor de voz
engine = pyttsx3.init()

# Obtención de las voces disponibles y selección de la primera voz
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 145)
for voice in voices:
    print(voice)