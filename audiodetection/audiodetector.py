import speech_recognition as sr
import webbrowser
import time

ONE_PIECE = "https://www.youtube.com/watch?v=QxpdFxnyrgw&autoplay=1&t=49"
CLOD = "https://www.youtube.com/watch?v=DvMOJymisNI&t=2s&autoplay=1"

def listen_for_keywords():
    recognizer = sr.Recognizer()
    #This index of 1 is a VB Cable output, this means that the 
    #desktop audio is routed into an input for the recognizer
    #this does require VB audio cable or use of stereo mixer
    with sr.Microphone(1) as source:
        print("Starting to Listen...")

        while True:
            try:
                audio = recognizer.listen(source)
                text = recognizer.recognize_google(audio).lower()
                print(f"Recorded: {text}")

                if "one piece" in text:
                    print("One Piece!")
                    webbrowser.open(ONE_PIECE)
                    time.sleep(5)
                if "clod" in text:
                    print("An act of CLOD!")
                    webbrowser.open(CLOD)
                    time.sleep(5)
                if "sus" in text:
                    print("SUS!")
                    time.sleep(5)

            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError:
                print("API unavailable")

def microphone_devices():
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        print(f"Device Index: {index}, Device Name: {name}")

listen_for_keywords()
#microphone_devices()