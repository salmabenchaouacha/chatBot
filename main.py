import os
from dotenv import load_dotenv
import openai
import google.generativeai as genai

# Charger les clés depuis le fichier .env
load_dotenv()

# OpenAI API Key
openai_api_key = os.getenv("OPENAI_API_KEY")

# Gemini API Key (doit être GOOGLE_API_KEY)
google_api_key = os.getenv("GOOGLE_API_KEY")

# Configuration OpenAI
openai_client = openai.OpenAI(api_key=openai_api_key)

# Configuration Gemini
genai.configure(api_key=google_api_key)
gemini_model = genai.GenerativeModel(model_name="models/gemini-1.5-pro")

# Historique pour OpenAI uniquement
openai_messages = [{"role": "system", "content": "You are a data science tutor who provides short, simple explanations."}]

# Sélection du modèle
model_choice = input("Choisir le modèle [openai/gemini] : ").strip().lower()

def chat_with_openai(prompt):
    openai_messages.append({"role": "user", "content": prompt})
    response = openai_client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=openai_messages
    )
    reply = response.choices[0].message.content.strip()
    openai_messages.append({"role": "assistant", "content": reply})
    return reply

def chat_with_gemini(prompt):
    response = gemini_model.generate_content(prompt)
    return response.text.strip()

if model_choice not in ["openai", "gemini"]:
    print("❌ Modèle non reconnu. Choisis 'openai' ou 'gemini'.")
    exit()

print(f"✅ Modèle sélectionné : {model_choice.upper()}")
print("💬 Chatbot démarré. Tape 'exit' pour quitter.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("👋 Fin de session.")
        break

    if model_choice == "openai":
        print("Assistant:", chat_with_openai(user_input), "\n")
    else:
        print("Assistant:", chat_with_gemini(user_input), "\n")
