import speech_recognition as sr
import webbrowser
import time

# The YouTube link to open when "One Piece" is detected
ONE_PIECE = "https://www.youtube.com/watch?v=QxpdFxnyrgw&autoplay=1&t=49"
CLOD = "https://www.youtube.com/watch?v=DvMOJymisNI&t=2s&autoplay=1"

def listen_for_keywords():
    recognizer = sr.Recognizer()
    #stereo mix on device number
    with sr.Microphone(1) as source:
        print("Listening ")

        # Continuously listen for audio
        while True:
            try:
                # Capture audio from the source
                audio = recognizer.listen(source)

                # Recognize speech using Google Web Speech API
                text = recognizer.recognize_google(audio).lower()
                print(f"Detected speech: {text}")

                # Check if "one piece" is mentioned
                if "one piece" in text:
                    print("One Piece!")
                    # Open the YouTube link
                    webbrowser.open(ONE_PIECE)
                    # Adding a delay to prevent opening multiple tabs in quick succession
                    time.sleep(5)
                if "clod" in text:
                    print("an act of CLOD!")
                    # Open the YouTube link
                    webbrowser.open(CLOD)
                    # Adding a delay to prevent opening multiple tabs in quick succession
                    time.sleep(5)
                if "stop" in text:
                    break

            except sr.UnknownValueError:
                # In case speech is not recognized, continue listening
                print("Could not understand audio")
            except sr.RequestError:
                # In case of issues with the API, print an error
                print("API unavailable")

def microphone_devices():
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        print(f"Device Index: {index}, Device Name: {name}")

# Run the function
listen_for_keywords()
#microphone_devices()