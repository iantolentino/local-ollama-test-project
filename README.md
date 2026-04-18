# Local Ollama Gym AI Assistant

A local AI chatbot built using Ollama, FastAPI, and a web-based UI.
It is designed as a lightweight gym and workout assistant that runs fully offline after setup.

---

## Features

* Local LLM via Ollama (no API costs)
* FastAPI backend server
* Web-based chat UI (HTML, CSS, JavaScript)
* Gym/workout-focused AI responses
* Markdown-formatted responses (clean readable output)
* AI “thinking” indicator in UI
* Optimized for faster model inference using phi3
* Fully offline after setup

---

## Tech Stack

* Python
* FastAPI
* Ollama
* HTML, CSS, JavaScript (vanilla frontend)

---

## Requirements

### Install dependencies

* Python 3.9+
* Ollama → [https://ollama.com](https://ollama.com)
* A local model (recommended: phi3)

### Pull model

```bash
ollama pull phi3
```

---

## Setup

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

Ensure Ollama is running and the model is available:

```bash
ollama run phi3
```

---

### 4. Start FastAPI server

```bash
uvicorn app:app --reload
```

---

### 5. Open application

Open in browser:

```
http://127.0.0.1:8000
```

---

## How it works

1. User enters a message in the web UI
2. Frontend sends request to FastAPI `/chat`
3. FastAPI forwards request to Ollama API
4. Phi-3 model generates a response
5. Response is returned and rendered in Markdown format in the UI
6. “AI is thinking” indicator is replaced with final output

---

## Project Structure

```
pj1/
│
├── app.py
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   └── script.js
├── README.md
└── .gitignore
```

---

## Model Configuration

Default model:

```
phi3:latest
```

You can change the model inside `app.py`:

```python
"model": "phi3:latest"
```

To check available models:

```bash
ollama list
```

---

## Notes

* Ensure Ollama is running before starting FastAPI
* Model name must exactly match installed Ollama model
* First request may be slower due to model loading (cold start)
* Performance improves significantly after first load (warm cache)

---

## Performance Considerations

To improve speed:

* Use smaller models (phi3 is recommended over mistral)
* Keep Ollama running in background
* Avoid restarting model frequently
* Reduce prompt length in system instructions if needed

---

## Future Improvements

* Streaming responses (token-by-token output like ChatGPT)
* Conversation memory (chat history persistence)
* Enhanced UI (sidebar chat sessions, animations)
* Workout tracking and progression system
* Exportable workout plans (PDF/JSON)
* Desktop app version (Electron or Tauri)

---

## Author

Built as a learning project for integrating local LLMs with Python, FastAPI, and Ollama.
Focus: gym-focused AI assistant with offline capability.

