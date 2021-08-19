import serial
import speech_recognition as sr
import time 


valid_commands = ['on', 'off']
target = serial.Serial('/dev/cu.usbmodem142101', 9600)

def write_serial(input_text):
    target.write(input_text.encode())
    time.sleep(0.5)
    target.readline()

recognizer = sr.Recognizer()

def get_voice_command():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            text = text.lower() + '\n'
            return text
        except sr.UnknownValueError:
            print("Could not understand audio")

while True:
    print("Waiting for input")
    input_text = get_voice_command()
    print(input_text, end="")
    if input_text in valid_commands:
        write_serial(input_text)
    else:
        print("Invalid command")