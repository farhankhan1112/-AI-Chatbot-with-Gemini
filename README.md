# AI Chatbot with Gemini

This is a simple AI chatbot built using Google Generative AI (Gemini) and Streamlit. The chatbot allows users to ask questions and receive AI-generated responses.

![Alt text](image-url)


## Features
- Uses Google Generative AI (Gemini) for natural language processing
- Streamlit-based UI for easy interaction
- Maintains chat history within a session
- Simple and lightweight implementation

## Requirements
- Python 3.8+
- Streamlit
- Google Generative AI SDK

## Installation
1. Clone this repository or download the source code.
2. Install the required dependencies:
   ```sh
   pip install streamlit google-generativeai
   ```
3. Obtain a Google Generative AI API key from [Google AI](https://ai.google.dev/)
4. Replace `api_key` in the script with your API key.

## Usage
Run the chatbot using the following command:
```sh
streamlit run app.py
```
Then, open the provided local URL in your browser and start chatting.

## Code Explanation
- The script initializes the Gemini AI model using an API key.
- It sets up a Streamlit UI with an input field and chat history.
- User inputs are processed, and responses are generated using Gemini AI.
- The chat history is stored in the session state to maintain continuity.

## Notes
- Ensure that your API key is valid and has the necessary permissions.
- This chatbot is intended for basic interactions and may require modifications for advanced use cases.

## License
This project is open-source. Feel free to modify and use it as needed.

