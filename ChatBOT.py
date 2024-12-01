import streamlit as st
import os
import subprocess
import platform
import speech_recognition as sr
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    """Speak the given text."""
    engine.say(text)
    engine.runAndWait()

def open_application(app_name):
    """Open an application based on the given name or path."""
    try:
        if platform.system() == "Windows":
            os.startfile(app_name)
        elif platform.system() == "Darwin":  # macOS
            subprocess.call(["open", app_name])
        elif platform.system() == "Linux":  # Linux
            subprocess.call(["xdg-open", app_name])
        else:
            return "Unsupported operating system."
        return f"{app_name} is opening!"
    except Exception as e:
        return f"Error: {e}"

def listen_command():
    """Listen to the user's voice command and return the transcribed text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Listening for a voice command...")
        try:
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio)
            return command
        except sr.UnknownValueError:
            return "Sorry, I couldn't understand your command."
        except sr.RequestError:
            return "Could not request results from Google Speech Recognition."
        except Exception as e:
            return f"Error: {e}"

# Streamlit UI
st.title("Voice Command Application Launcher")
st.write("Use your voice to command your computer to open applications.")

# Button to activate voice command
if st.button("Speak Command"):
    command = listen_command()
    st.write(f"You said: {command}")
    speak(f"You said: {command}")
    if command.lower() in ["exit", "close", "stop"]:
        speak("Exiting the application launcher.")
    elif command.strip():
        result = open_application(command)
        st.success(result)
        speak(result)
    else:
        st.error("No valid command detected. Please try again.")
