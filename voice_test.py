import pyttsx3

nova = pyttsx3.init()

while True:
    message = input("Type something: ")

    if message == "exit":
        break

    print("Speaking:", message)
    nova.say(message)
    print("Starting playback...")

    nova.runAndWait()

    print("Playback finished!")