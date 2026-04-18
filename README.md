# 🧠 Local Ollama Gym AI Assistant

A simple local AI chatbot built using **Ollama + FastAPI + HTML UI**.  
Designed as a lightweight **gym/workout-focused AI assistant** that runs completely offline.

---

## 🚀 Features

- Local LLM via Ollama (no API cost)
- FastAPI backend
- Simple browser-based chat UI
- Gym/workout-focused AI responses
- Fully offline after setup

---

## 🧱 Tech Stack

- Python
- FastAPI
- Ollama
- HTML + JavaScript (vanilla)

---

## 📦 Requirements

Install:

- Python 3.9+
- Ollama → https://ollama.com
- A model (example: mistral)

Pull model:

```bash
ollama pull mistral
````

---

## ⚙️ Setup

### 1. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 2. Install dependencies

```bash
pip install fastapi uvicorn requests
```

---

### 3. Run Ollama

Make sure Ollama is running:

```bash
ollama run mistral:latest
```

---

### 4. Start server

```bash
uvicorn app:app --reload
```

---

### 5. Open in browser

```
http://127.0.0.1:8000
```

---

## 💬 How it works

1. User enters prompt in browser
2. FastAPI receives request
3. Request is sent to Ollama
4. Model generates response
5. Response is shown in UI

---

## 📁 Project Structure

```
pj1/
│
├── app.py
├── README.md
├── .gitignore
└── venv/ (ignored)
```

---

## 🧠 Current Model

Default:

```
mistral:latest
```

Change inside `app.py` if needed.

---

## ⚠️ Notes

* This is a local-only AI project
* No cloud API keys required
* Ensure Ollama is running before starting FastAPI
* Model name must match `ollama list` exactly

---

## 🏗️ Future Improvements

* Chat memory (conversation history)
* Streaming responses (typing effect)
* Better UI (ChatGPT-style interface)
* Gym-only strict mode enforcement
* Desktop app packaging (Electron / Tauri)

---

## 🧑‍💻 Author

Built as a learning project for local LLM integration using Python + Ollama + FastAPI.

```
