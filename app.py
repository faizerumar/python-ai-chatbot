import streamlit as st
from google import genai

st.set_page_config(page_title="Spectsman AI Chatbot", page_icon="🤖")
st.title("🤖 Spectsman AI Chatbot")
st.write("A friendly coding assistant powered by Google Gemini, created by Umar Faizer")

# Initialize the client and chat session in st.session_state so they persist across re-runs
if "client" not in st.session_state:
    try:
        # Tries to load key from Streamlit secrets, falls back to environment variables
        api_key = st.secrets.get("GEMINI_API_KEY", None)
        if api_key:
            st.session_state.client = genai.Client(api_key=api_key)
        else:
            st.session_state.client = genai.Client()
    except Exception as e:
        st.error(f"Failed to initialize client. Check your API key configuration: {e}")
        st.stop()

if "chat" not in st.session_state:
    st.session_state.chat = st.session_state.client.chats.create(
        model="gemini-3.6-flash",
        config={
            "system_instruction": "You are a helpful, friendly, and concise coding assistant.",
            "temperature": 0.7
        }
    )
    st.session_state.messages = []

# Display past conversation history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Capture user input from the chat box
if user_input := st.chat_input("Type your coding question here..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                # Uses the persistent chat session bound to the active client
                response = st.session_state.chat.send_message(user_input)
                bot_reply = response.text
            except Exception as e:
                bot_reply = f"An error occurred: {e}"
            
            st.markdown(bot_reply)
            st.session_state.messages.append({"role": "assistant", "content": bot_reply})