
import speech_recognition as sr
import pyttsx3
from datetime import datetime

# Create a speech recognizer
recognizer = sr.Recognizer()

# Initialize NOVA's voice engine
nova = pyttsx3.init()

# Select Microsoft Zira voice
voices = nova.getProperty("voices")
nova.setProperty("voice", voices[1].id)


# Make NOVA speak
def speak(text):
    print("NOVA:", text)
    nova.say(text)
    nova.runAndWait()


# Interpret NOVA's commands
def process_command(command):
    command = command.lower().strip()

    if command == "hello":
        speak("Hello! How can I help you?")

    elif command == "time":
        current_time = datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}")

    elif command == "date":
        current_date = datetime.now().strftime("%d %B %Y")
        speak(f"Today is {current_date}")

    elif command == "who are you":
        speak("I am NOVA, your personal voice assistant.")

    elif command == "who created you":
        speak("I was created by Christopher Wesala.")

    elif command == "help":
        speak("I understand hello, time, date, who are you, who created you, and exit.")

    elif command == "exit":
        speak("Goodbye!")
        return False

    else:
        speak("I don't understand that command yet.")

    return True


# Access the microphone
microphone = sr.Microphone()


# Start NOVA
with microphone as source:

    print("NOVA: Calibrating microphone...")
    recognizer.adjust_for_ambient_noise(source, duration=2)

    print("NOVA: Microphone ready!")

    while True:

        print("\nNOVA: Waiting for wake phrase...")

        try:
            audio = recognizer.listen(source)
            phrase = recognizer.recognize_google(audio)

            print("You:", phrase)

            if "hey nova" in phrase.lower():

                speak("I'm listening!")

                print("NOVA: Listening for your command...")

                command_audio = recognizer.listen(source)

                command = recognizer.recognize_google(command_audio)

                print("You:", command)

                if not process_command(command):
                    break

        except sr.UnknownValueError:
            print("NOVA: Sorry, I didn't catch that.")

        except sr.RequestError:
            speak("I cannot connect to the speech recognition service.")
            break
