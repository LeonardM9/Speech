import speech_recognition as sr
import subprocess
import pyautogui

recognizer = sr.Recognizer()
proceso = None
saludo = """ hola buenas"""

def ejecutar_comando(comando):
    global proceso
    if "open notepad" in comando:
        proceso = subprocess.Popen(["notepad.exe"])
    elif "saludo" in comando:
        pyautogui.write(saludo)
    elif "cerrar notepad" in comando: 
        proceso.terminate()

def escucha_comando():
    with sr.Microphone() as source: 
        print("En que puedo ayudarte")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        comando = recognizer.recognize_bing(audio, language="en-US")
        print(f"comando reconocido: {comando}")
        ejecutar_comando(comando)
    except sr.UnknownValueError:
        print("No se pudo entender el comando")

while True:
    escucha_comando()
