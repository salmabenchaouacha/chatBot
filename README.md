# 🤖 AI Chatbot: OpenAI & Gemini (Google) API Integration

This is a simple command-line chatbot that allows you to choose between using the **OpenAI GPT models** (like GPT-3.5 or GPT-4) and **Gemini** models (like Gemini 1.5 Pro) via the **Google Generative AI API**.

## 🧰 Features


- **Runtime selection between OpenAI and Gemini**  
  The project allows choosing which GPT provider to use (OpenAI or Gemini) dynamically at runtime without changing the source code.

- **Secure API key loading via `.env` file**  
  API keys are stored in a local `.env` file that is excluded from version control, keeping sensitive information safe.  
  The project uses the `python-dotenv` library to automatically load these environment variables.

- **Conversation history support for OpenAI**  
  Maintains chat context to enable coherent and relevant responses in ongoing conversations.

- **Minimal and clean codebase**  
  The code is simple, readable, and maintainable by following best practices like environment variable management and clear modular structure.

