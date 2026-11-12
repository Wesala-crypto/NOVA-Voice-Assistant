
# NOVA - PERSONAL VOICE ASSISTANT

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
    respond("Hello! How can I help you today?")


# Introduction function
def introduce():
    respond(
        "I am NOVA, your personal voice assistant. "
        "How may I help you today?"
    )


# Tell the current time
def tell_time():
    current_time = datetime.now().strftime("%I:%M %p")
    respond(f"The current time is {current_time}.")


# Tell the current date
def tell_date():
    current_date = datetime.now().strftime("%d %B %Y")
    respond(f"Today's date is {current_date}.")


# Explain NOVA's purpose
def explain_purpose():
    respond(
        "I was created to serve as a personal voice assistant. "
        "My purpose is to make everyday tasks easier through voice commands, "
        "provide useful information, and help people interact "
        "with their computers and phones hands-free."
    )


# Explain what NOVA can do
def explain_capabilities():
    respond(
        "I can greet you, introduce myself, tell you the current time "
        "and date, and answer questions about my identity and purpose. "
        "Currently, I am still learning new abilities for improvement."
    )


# Help function
def show_help():
    respond(
        "You can ask me to say hello, tell you the time or date, "
        "introduce myself, explain my purpose, or tell you who created me. "
        "You can also say exit to shut me down."
    )


# Clean and normalize user input
def normalize_input(command):
    command = command.lower().strip()

    for character in "?!.,":
        command = command.replace(character, "")

    return command


# NOVA's intent dictionary
intents = {
    "exit": [
        "exit", "quit", "shut down",
        "goodbye", "bye", "see you"
    ],

    "greeting": [
        "hello", "hi", "hey",
        "good morning", "good afternoon", "good evening"
    ],

    "introduction": [
        "who are you", "what is your name",
        "what's your name", "tell me about yourself",
        "introduce yourself", "your identity"
    ],

    "creator": [
        "who created you", "who made you",
        "who built you", "who developed you",
        "who is your creator", "who is your developer"
    ],

    "purpose": [
        "why were you created", "what is your purpose",
        "why do you exist", "what were you made for",
        "what is your mission", "what is your reason for existing"
    ],

    "capabilities": [
        "what can you do", "what are your abilities",
        "what are your capabilities", "how can you help me",
        "what do you do"
    ],

    "time": [
        "time", "what time is it",
        "tell me the time", "what is the time", "current time"
    ],

    "date": [
        "date", "what is today's date",
        "what is the date", "tell me the date",
        "today's date"
    ],

    "help": [
        "help", "what commands", "commands"
    ]
}


# Remember the current conversation topic
conversation_topic = None


# Check whether a question matches any known phrase
def matches(command, phrases):
    return any(
        command == phrase
        or command.startswith(phrase + " ")
        or (" " + phrase + " ") in (" " + command + " ")
        for phrase in phrases
    )


# Identify the user's intention
def recognize_intent(command):
    for intent, phrases in intents.items():

        if matches(command, phrases):
            return intent

    return "unknown"


# Process user commands
def process_command(command):

    global conversation_topic

    # Identify the user's intention
    intent = recognize_intent(command)

    # Handle follow-up questions before changing the topic
    if intent == "unknown":

        if conversation_topic == "creator":

            follow_up_phrases = [
                "tell me more",
                "more about him",
                "more about my creator",
                "who is he",
                "what does he do"
            ]

            if any(phrase in command for phrase in follow_up_phrases):
                respond(
                    "You're asking about my creator, Christopher Wesala. "
                    "I don't have more personal information about him yet."
                )
                return True

    # Remember a newly recognized topic
    if intent != "unknown":
        conversation_topic = intent

    # Exit
    if intent == "exit":
        respond("Goodbye! See you later.")
        return False

    # Greeting
    elif intent == "greeting":
        greet()

    # Introduction
    elif intent == "introduction":
        introduce()

    # Creator
    elif intent == "creator":
        respond("I was created by Christopher Wesala.")

    # Purpose
    elif intent == "purpose":
        explain_purpose()

    # Capabilities
    elif intent == "capabilities":
        explain_capabilities()

    # Time
    elif intent == "time":
        tell_time()

    # Date
    elif intent == "date":
        tell_date()

    # Help
    elif intent == "help":
        show_help()

    # Unknown commands
    else:
        respond(
            "I'm sorry, I don't understand that question yet. "
            "You can ask me for help to see what I can do."
        )

    return True


# Main NOVA program
def start_nova():

    print("==============================")
    print("       NOVA ASSISTANT")
    print("==============================")
    print("NOVA is online!")
    print("Type 'help' to see available commands.")
    print("Type 'exit' to shut down NOVA.")
    print("NOVA is ready to help.")

    respond("NOVA is online. How can I help you?")

    while True:

        command = normalize_input(input("You: "))

        if not command:
            continue

        if not process_command(command):
            break


# Start NOVA
if __name__ == "__main__":
    start_nova()
