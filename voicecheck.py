import pyttsx3


def say(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')

    # Set the desired Microsoft Guy Natural Voice
    for voice in voices:
        if "guy" in voice.name.lower():
            engine.setProperty('voice', voice.id)
            break

    engine.say(text)
    engine.runAndWait()


# Example usage:
say("Hello, I am your assistant. How can I help you?")
