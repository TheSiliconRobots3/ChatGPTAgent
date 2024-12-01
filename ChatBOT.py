import streamlit as st
import os

# List of common applications and their paths
apps = {
    "Notepad": "notepad.exe",
    "Calculator": "calc.exe",
    "Paint": "mspaint.exe",
    "File Explorer": "explorer.exe",
    "Command Prompt": "cmd.exe",
    "Microsoft Edge": "msedge.exe",
    "Google Chrome": "chrome.exe",
    "VLC Media Player": "vlc.exe",  # Ensure VLC is installed
    "Spotify": "spotify.exe",       # Ensure Spotify is installed
}

# Streamlit UI
st.set_page_config(page_title="App Launcher", page_icon="💻")

# Header with icons
st.markdown(
    """
    <h1 style='text-align: center;'>💻 Windows Application Launcher</h1>
    <p style='text-align: center;'>Select an application from the list below and click Launch!</p>
    """,
    unsafe_allow_html=True,
)

# Dropdown to select application
selected_app = st.selectbox(
    "Choose an application to open:",
    options=list(apps.keys()),
    help="Select an application and click 'Launch' to open it.",
)

# Launch button
if st.button("🚀 Launch Application"):
    try:
        # Open the selected application
        os.system(apps[selected_app])
        st.success(f"Successfully launched {selected_app}!")
    except Exception as e:
        st.error(f"Failed to launch {selected_app}. Error: {e}")

# Footer
st.markdown(
    """
    <hr>
    <p style='text-align: center;'>Made with ❤️ using Streamlit</p>
    """,
    unsafe_allow_html=True,
)
