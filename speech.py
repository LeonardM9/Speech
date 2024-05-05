import speech_recognition as sr
import subprocess
import pyautogui

recognizer = sr.Recognizer()
proceso = None
saludo = """ hola buenas"""

def ejecutar_comando(comando):
    global proceso
    if "abrir bloc de notas" in comando:
        proceso = subprocess.Popen(["notepad.exe"])
    elif "saludo" in comando:
        pyautogui.write(saludo)
    elif "cerrar notepad" in comando: 
        proceso.terminate()
    while "salir del programa" in comando:
        break
        

def escucha_comando(): 
    with sr.Microphone() as source: 
        print("En que puedo ayudarte")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        comando = recognizer.recognize_google(audio, language="es-ES")
        print(f"comando reconocido: {comando}")
        ejecutar_comando(comando)
    except sr.UnknownValueError:
        print("No se pudo entender el comando")

while True:
    escucha_comando()
