# AI Chatbot with Gemini

- This is a simple **AI chatbot** built using **Google Generative AI (Gemini)** and **Streamlit**. The chatbot leverages a **Large Language Model (LLM)** to understand user questions and 
 generate intelligent, context-aware AI responses in real-time.

# Project interface: 
- Interactive chat interface
- Powered by Gemini AI for natural language understanding
- Easy-to-use 

![Alt text](https://github.com/farhankhan1112/AI-Chatbot-with-GenAI/blob/17e75b3692fba2f88f7cd4e050160436fe99a740/Images/project%20inerface.png)

# project output :
![Alt text](https://github.com/farhankhan1112/AI-Chatbot-with-GenAI/blob/17e75b3692fba2f88f7cd4e050160436fe99a740/Images/project%20output.png)

# 1️⃣ User Input : 
- The user types a message or question in the chatbot interface (Your message text box).
- Example: "How are you?"

# 2️⃣ API Call to Gemini :
- When the user sends a message, the backend code makes an API call to Google Gemini (via Gemini API).
- The input message is sent as a prompt to the Gemini API for generating a response.

# 3️⃣ AI Response Generation :
- The Gemini API processes the input and generates a relevant response based on its large language model (LLM).
- Example Response: "I'm doing well, thank you for asking! How are you today?"

# 4️⃣ Display Response :
- The AI-generated response is displayed in the chat interface.
- The user sees a conversational reply, just like chatting with an AI assistant.

# 🛠️ Technologies Used in the AI Chatbot Project
- 👨‍💻 Programming Language: Python

- 🌐 Web Framework: Streamlit

- 🧠 Large Language Model (LLM): Gemini 1.5 Pro (via Google Generative AI API)

- 🔌 API Integration: Google Generative AI (for using Gemini LLM)

- 💬 Chat UI: Streamlit chat_message() for chat-style interface

- 🗂️ State Management: Streamlit session_state (to store chat history)

- 🔐 Authentication: API Key for Google Generative AI

# Requirements
- Python 3.8+
- Streamlit
- Google Generative AI SDK

#Installation
1. Clone this repository or download the source code.
2. Install the required dependencies:
   ```sh
   pip install streamlit google-generativeai
   ```
3. Obtain a Google Generative AI API key from [Google AI](https://ai.google.dev/)
4. Replace `api_key` in the script with your API key.

# Usage
Run the chatbot using the following command:
```sh
streamlit run app.py
```
Then, open the provided local URL in your browser and start chatting.

# Code Explanation
- The script initializes the Gemini AI model using an API key.
- It sets up a Streamlit UI with an input field and chat history.
- User inputs are processed, and responses are generated using Gemini AI.
- The chat history is stored in the session state to maintain continuity.

# Notes
- Ensure that your API key is valid and has the necessary permissions.
- This chatbot is intended for basic interactions and may require modifications for advanced use cases.

## License
This project is open-source. Feel free to modify and use it as needed.

