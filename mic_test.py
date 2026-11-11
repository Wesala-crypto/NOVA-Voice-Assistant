
import speech_recognition as sr
import pyttsx3
from datetime import datetime

# Create a recognizer
recognizer = sr.Recognizer()

# Initialize NOVA's voice engine
nova = pyttsx3.init()

# Select Microsoft Zira voice
voices = nova.getProperty("voices")
nova.setProperty("voice", voices[1].id)


# Access the microphone
with sr.Microphone() as source:

    print("NOVA: Adjusting for background noise...")
    recognizer.adjust_for_ambient_noise(source, duration=2)

    print("NOVA: I'm listening. Speak now!")

    # Keep listening until the user says exit
    while True:

        audio = recognizer.listen(source)

        print("NOVA: Processing your speech...")

        try:
            # Convert speech into text
            text = recognizer.recognize_google(audio)
            print("You:", text)

            # Interpret the command
            command = text.lower().strip()

            if command == "hello":
                response = "Hello! How can I help you?"

            elif command == "time":
                current_time = datetime.now().strftime("%I:%M %p")
                response = f"The time is {current_time}"

            elif command == "date":
                current_date = datetime.now().strftime("%d %B %Y")
                response = f"Today is {current_date}"

            elif command == "who are you":
                response = "I am NOVA, your personal voice assistant."

            elif command == "who created you":
                response = "I was created by Christopher Wesala."

            elif command == "help":
                response = "I understand hello, time, date, who are you, who created you, and exit."

            elif command == "exit":
                response = "Goodbye!"
                print("NOVA:", response)
                nova.say(response)
                nova.runAndWait()
                break

            else:
                response = "I don't understand that command yet."

            # Display and speak the response
            print("NOVA:", response)
            nova.say(response)
            nova.runAndWait()

        except sr.UnknownValueError:
            print("NOVA: Sorry, I didn't understand that.")

        except sr.RequestError:
            print("NOVA: I cannot connect to the speech recognition service.")
            break
