import google.generativeai as genai

genai.configure(api_key="AIzaSyDW4RG9mQM-2chVL0UJhuhCGE3VmlRuq7A")

# List available models
models = genai.list_models()
for model in models:
    print(model.name)


import streamlit as st
import google.generativeai as genai

# Configure Gemini API


model = genai.GenerativeModel("gemini-1.5-pro")  # Replace with your available model name


# Streamlit UI
st.title("💬 AI Chatbot with Gemini")
st.write("Ask me anything!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input field for user message
user_input = st.text_input("Your message:", key="user_input")

if user_input:
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Get response from Gemini AI
    response = model.generate_content(user_input)

    # Add AI response to chat history
    bot_reply = response.text
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})

    # Display AI response
    with st.chat_message("assistant"):
        st.markdown(bot_reply)
