import streamlit as st

# Streamlit page configuration
st.set_page_config(
    page_title="ChatGPT Replica",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Persistent state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar: Application Info
st.sidebar.title("ChatGPT Replica")
st.sidebar.markdown("""
This is a simple replica of OpenAI's ChatGPT interface built using Streamlit.
- Chat with an AI assistant.
- Messages are displayed in a conversational format.
""")

# Main Header
st.markdown(
    "<h1 style='text-align: center;'>ChatGPT Replica</h1>",
    unsafe_allow_html=True,
)

# Chat History Display
st.markdown("### Chat History")
chat_container = st.container()

# Display Chat Messages
with chat_container:
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.markdown(f"**🧑 User:** {msg['content']}")
        else:
            st.markdown(f"**🤖 Assistant:** {msg['content']}")

# User Input Section
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_area("Type your message:", placeholder="Ask anything...", height=100)
    submit_button = st.form_submit_button("Send")

# Handle User Input
if submit_button and user_input.strip():
    # Save user message to history
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Simulate Assistant Response
    assistant_response = f"You said: {user_input}"
    st.session_state.messages.append({"role": "assistant", "content": assistant_response})
    
    # Rerun to update the chat
    st.experimental_rerun()

# Clear Chat History
if st.button("Clear Chat"):
    st.session_state.messages = []
    st.experimental_rerun()
