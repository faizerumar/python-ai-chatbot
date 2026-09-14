from google import genai
import os

# Initialize the Gemini client (it will automatically look for the GEMINI_API_KEY environment variable)
client = genai.Client()

print("Initializing Cloud Chatbot using Google Gemini...")

# Create an interactive chat session
chat = client.chats.create(
    model="gemini-3.6-flash",
    config={
        "system_instruction": "You are a helpful, friendly, and concise coding assistant.",
        "temperature": 0.7
    }
)

print("\nChatbot is ready! Type 'exit' or 'quit' to end the conversation.\n")

# Main conversation loop
while True:
    try:
        user_input = input("You: ")
    except (KeyboardInterrupt, EOFError):
        print("\nChatbot: Goodbye!")
        break

    if user_input.strip().lower() in ["exit", "quit"]:
        print("Chatbot: Goodbye! Happy coding!")
        break

    if not user_input.strip():
        continue

    # Send the user input to the cloud chat session
    response = chat.send_message(user_input)

    print(f"Chatbot: {response.text}\n")