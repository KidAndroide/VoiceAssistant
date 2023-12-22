import pyttsx3
import speech_recognition as sr
import pywhatkit
import pyjokes
import webbrowser
import datetime
import tkinter as tk
from tkinter import font
from PIL import ImageTk
import ttkbootstrap as ttk


def audiotexto():
    r = sr.Recognizer()
    with sr.Microphone() as origen:
        r.pause_threshold = 0.8
        print("ya puedes hablar")
        audio = r.listen(origen)
        try:
            pedido = r.recognize_google(audio, language="es-ar")
            print("dijiste: " + pedido)
            return pedido
        except sr.UnknownValueError:
            print("disculpa no te he entendido")
            return "sigo esperando"
        except sr.RequestError:
            print("no entendi")
            return "sigo esperando"
        except:
            print("no entiendo")
            return "sigo esperando"

def hablar(mensaje):
    engine = pyttsx3.init()
    engine.setProperty('voice', id1)
    engine.say(mensaje)
    engine.runAndWait()

id1 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0'

def pedir_dia():
    dia = datetime.date.today()
    print(dia)
    dia_semana = dia.weekday()
    print(dia_semana)
    calendario = {0: 'lunes', 1: 'martes', 2: 'miércoles', 3: 'jueves', 4: 'viernes', 5: 'sábado', 6: 'domingo'}
    hablar(f'hoy es {calendario[dia_semana]}')

def pedir_hora():
    hora = datetime.datetime.now()
    hora = f'Son las {hora.hour} horas {hora.minute} minutos'
    print(hora)
    hablar(hora)

def saludo_inicial():
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = 'buenas noches'
    elif 6 <= hora.hour < 13:
        momento = 'buen día'
    else:
        momento = 'buenas tardes'
    hablar(f'{momento}. soy malu 9: ¿en qué puedo ayudarte?')

def pedir_cosas():
    saludo_inicial()
    comenzar = True
    while comenzar:
        pedido = audiotexto().lower()
        if 'abrir youtube' in pedido:
            hablar('Con gusto, estoy abriendo YouTube')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'abrir navegador' in pedido:
            hablar('Claro, estoy en eso')
            webbrowser.open('https://www.google.com')
            continue
        elif 'qué día es' in pedido:
            pedir_dia()
            continue
        elif 'qué hora es' in pedido:
            pedir_hora()
            continue
        elif 'busca' in pedido:
            hablar('buscando')
            pedido = pedido.replace('busca', '')
            pywhatkit.search(pedido)
            hablar('Esto es lo que he encontrado')
            continue
        elif 'reproducir' in pedido or 'escuchar'in pedido:
            hablar('Buena idea, reproduciendo')
            pywhatkit.playonyt(pedido)
            continue
        elif 'chiste' in pedido:
            hablar(pyjokes.get_joke('es'))
            continue
        elif 'otro' in pedido:
            hablar(pyjokes.get_joke('es'))
            continue
        elif 'hasta luego' in pedido:
            hablar("besis, nos re vimos!")
            break


def iniciar_programa():
    pedir_cosas()


root = tk.Tk()

canvas = tk.Canvas(root, width=400, height=300)
canvas.grid(columnspan=3)


logo_img = ImageTk = ImageTk.PhotoImage(file="img/robologo.png")
logowid = tk.Label(canvas, image=logo_img)
logowid.image = logo_img
logowid.pack()

tk.Button(canvas, text="SPEAK", font=("TKMenuFont", 20), bg="#1affff", fg="black",
          command=iniciar_programa) .pack()




root.mainloop()