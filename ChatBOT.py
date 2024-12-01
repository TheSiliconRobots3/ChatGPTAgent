import streamlit as st
import os
import subprocess
import platform

# Function to open applications
def open_application(app_name):
    try:
        if platform.system() == "Windows":
            os.startfile(app_name)  # Windows-specific
        elif platform.system() == "Darwin":  # macOS
            subprocess.call(["open", app_name])
        elif platform.system() == "Linux":  # Linux
            subprocess.call(["xdg-open", app_name])
        else:
            return "Unsupported OS."
        return f"Opening {app_name}!"
    except Exception as e:
        return f"Error: {e}"

# Streamlit UI
st.title("Simple Voice Command Application Launcher")
st.write("Enter the application name or path to open it.")

# Input text for command
app_name = st.text_input("Enter the application name or path (e.g., notepad, chrome, /usr/bin/firefox):")

# Button to trigger app opening
if st.button("Open Application"):
    if app_name.strip():
        result = open_application(app_name.strip())
        st.success(result)
    else:
        st.error("Please enter a valid application name or path.")
