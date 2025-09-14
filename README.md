# 💬 AI Chat Bot – Automated WhatsApp/Chat Responder  

This Python project is an **AI-powered auto chat bot** that uses **ChatGPT (OpenAI API)** along with **PyAutoGUI** and **Pyperclip** to automatically read messages from a chat window and send intelligent replies.  

It simulates human typing by copying AI-generated responses to the clipboard and pasting them into the chat app.  
---
🎤 Usage

Open WhatsApp Web (or another chat app).

Start the bot → it will:

Select chat messages

Copy text to clipboard

Send it to ChatGPT

Paste AI’s reply back into the chat
---

## 🚀 Features  
- 🔄 Reads chat messages automatically (using clipboard + PyAutoGUI drag)  
- 🤖 AI responses powered by **OpenAI GPT models**  
- 📋 Copies and pastes replies into the chat box automatically  
- 🖱️ Mouse automation for selecting text and clicking on input box  
- 🌐 Works with WhatsApp Web / other chat apps (with coordinate adjustments)  

---

## 🛠️ Tech Stack  
- **Python 3.x**  
- **OpenAI API** – AI responses  
- **PyAutoGUI** – GUI automation (mouse & keyboard)  
- **Pyperclip** – clipboard handling  
- **Time** – delays for smoother execution  

---

## ⚙️ Installation  

1. Clone the repository

2. Install dependencies:
pip install -r requirements.txt

3.Add your OpenAI API Key in the code:
client = OpenAI(api_key="<ENTER YOUR API KEY HERE>")

4. Adjust the screen coordinates (x, y positions) in the script to match your system’s chat app window.

5.Run the bot:
python program.py
