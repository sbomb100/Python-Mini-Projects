import speech_recognition as sr
import webbrowser
import time



#using VB Audio Cable mixed with Voicemeeter banana
def swear_jar():
    money_owed = 0.01
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for Profanity!")

        while True:
            try:
                audio = recognizer.listen(source)
                text = recognizer.recognize_google(audio).lower()
                print(f"{text}")

                if "fuck" in text:
                    print(f"--I HEARD THAT YOUNG MAN!")
                    money_owed += 2.00
                if "shit" in text:
                    print(f"--WHAT DID YOU SAY?!")
                    money_owed += 1.75
                if "pussy" in text or "cunt" in text:
                    print(f"--respect women")
                    money_owed += 1.50
                if "ass" in text:
                    print(f"--its booty to you")
                    money_owed += 0.50
                if "piss" in text:
                    print(f"--cmon man")
                    money_owed += 0.25
                

                if "i am not a pedophile" in text:
                    print(f"-- You Owe: {money_owed}")
                    break

            except sr.UnknownValueError:
                print("** Could not understand audio")
            except sr.RequestError:
                print("** API unavailable")


def microphone_devices():
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        print(f"Device Index: {index}, Device Name: {name}")


swear_jar()
#microphone_devices()