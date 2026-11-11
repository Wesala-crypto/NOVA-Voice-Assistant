
# NOVA - Personal Voice Assistant

import pyttsx3
from datetime import datetime

# Initialize NOVA's voice engine
nova = pyttsx3.init()

# Select Microsoft Zira voice
voices = nova.getProperty("voices")
nova.setProperty("voice", voices[1].id)


# Make NOVA display and speak responses
def respond(text):
    print(f"NOVA: {text}")
    nova.say(text)
    nova.runAndWait()


# Greeting function
def greet():
    respond("Hello! How can I help you?")


# Introduction function
def introduce():
    respond("I am NOVA, your personal voice assistant. How may I help you?")


# Tell the current time
def tell_time():
    current_time = datetime.now().strftime("%I:%M %p")
    respond(f"The time is {current_time}")


# Tell the current date
def tell_date():
    current_date = datetime.now().strftime("%d %B %Y")
    respond(f"The date is {current_date}")


# Main NOVA program
def start_nova():

    print("========================")
    print("       NOVA ASSISTANT")
    print("========================")
    print("NOVA is online!")
    print("Type 'exit' to shut me down.")

    while True:

        command = input("You: ").lower().strip()

        if command == "exit":
            respond("Goodbye,see you later!")
            break

        elif command == "hello":
            greet()

        elif command == "time":
            tell_time()

        elif command == "date":
            tell_date()

        elif command == "who created you":
            respond("I was created by Christopher Wesala.")

        elif command == "who are you":
            introduce()

        elif command == "help":
            respond("Here are the commands I understand: hello, time, date, who created you, who are you, and exit.")

        else:
            respond("I don't understand that command yet.")


# Start NOVA
start_nova()
