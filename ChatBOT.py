import streamlit as st
import subprocess
import speech_recognition as sr

# List of common applications and their paths
apps = {
    "Notepad": "notepad.exe",
    "Calculator": "calc.exe",
    "Paint": "mspaint.exe",
    "File Explorer": "explorer.exe",
    "Command Prompt": "cmd.exe",
    "Microsoft Edge": "msedge.exe",
    "Google Chrome": "chrome.exe",  # Ensure Chrome is in PATH
    "VLC Media Player": "vlc.exe",  # Ensure VLC is installed
    "Spotify": "spotify.exe",       # Ensure Spotify is installed
}

# Streamlit UI
st.set_page_config(page_title="App Launcher", page_icon="🎙️")

# Header with icons
st.markdown(
    """
    <h1 style='text-align: center;'>🎙️ Windows Application Launcher</h1>
    <p style='text-align: center;'>Select or speak the application name to launch!</p>
    ""
