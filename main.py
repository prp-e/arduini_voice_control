import serial
import speech_recognition as sr
import time 

target = serial.Serial('/dev/cu.usbmodem142201', 9600)

def write_serial(input_text):
    target.write(input_text.encode())
    time.sleep(0.5)
    target.readline()

recognizer = sr.Recognizer()

def get_voice_command():
    with sr.Microphone() as source:
        recognizer.pause_threshold = 0.5
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio, language='fa')
            return text
        except sr.UnknownValueError:
            print("Could not understand audio")

while True:
    print("Waiting for input")
    input_text = get_voice_command()
    print(input_text)
    if input_text == 'قرمز':
        write_serial('r')
    elif input_text == 'زرد':
        write_serial('y')
    elif input_text == 'خداحافظ':
        exit()