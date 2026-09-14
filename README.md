# 🤖 Python AI Chatbot (Cloud-Powered & Secure)

A lightweight, cloud-powered AI chatbot built with **Python**, **Streamlit**, and the **Google GenAI SDK** (`google-genai`). This application connects directly to Google's Gemini cloud infrastructure, resulting in **0 bytes of local model storage** while providing a rich, interactive web UI.

---

## 🚀 Features
* **Zero Local Storage:** No heavy 3GB+ model files to download or run locally; all heavy lifting is processed via Google's cloud API.
* **Interactive Web UI:** Built with Streamlit for a clean, modern chat interface with real-time streaming responses and session memory.
* **Secure Architecture:** Built-in safeguards using environment variables and Streamlit secrets (`secrets.toml`) to prevent accidental API key leaks on GitHub.

---

## 🛠️ Technology Stack
* **Python** (Core application logic)
* **Streamlit** (Web-based user interface)
* **Google GenAI SDK** (`google-genai`)
* **Google Gemini API** (`gemini-3.6-flash`)

---

## ⚙️ Setup and Installation Instructions

### 1. Clone the Repository
Clone this repository to your local machine:
```bash
git clone [https://github.com/your-username/your-repository-name.git](https://github.com/your-username/your-repository-name.git)
cd python-chatbot
