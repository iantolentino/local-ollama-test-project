
# Local Ollama Gym AI Assistant

A fully local AI chatbot built with **Ollama**, **FastAPI**, and a lightweight web interface.
Designed as a **gym and workout–focused assistant** that runs entirely offline after initial setup.

This project demonstrates how to integrate local LLMs into a production-style web application without relying on paid APIs or cloud services.

---

## Key Features

* Local LLM inference via Ollama (no API costs)
* FastAPI backend with streaming responses
* Clean, ChatGPT-style web UI
* Gym and workout–focused prompt design
* Markdown-formatted responses for readability
* AI “thinking” indicator during generation
* Optimized for fast inference using `phi3`
* Fully offline operation after setup

---

## Technology Stack

* Python 3.9+
* FastAPI
* Ollama
* HTML, CSS, JavaScript (vanilla frontend)

---

## Requirements

### System Requirements

* Python 3.9 or newer
* Ollama installed and running
  [https://ollama.com](https://ollama.com)

### Supported Models

Recommended:

* `phi3:mini` (best balance of speed and quality)

Optional:

* `gemma:2b` (fastest)
* `llama3.2:3b` (better long-form reasoning)

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/iantolentino/local-ollama-test-project.git
cd local-ollama-test-project
```

---

### 2. Create and activate a virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3. Install Python dependencies

```bash
pip install fastapi uvicorn requests
```

---

### 4. Pull an Ollama model

```bash
ollama pull phi3:mini
```

Verify installation:

```bash
ollama list
```

---

### 5. Start the FastAPI server

```bash
uvicorn app:app --reload
```

---

### 6. Open the application

Open your browser and navigate to:

```
http://127.0.0.1:8000
```

---

## How It Works

1. User submits a message via the web interface
2. Frontend sends a request to the FastAPI `/chat` endpoint
3. FastAPI forwards the prompt to Ollama’s local API
4. The selected model generates a streamed response
5. Output is rendered in Markdown format in the UI
6. “Thinking” indicator is replaced by the final response

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

The active model is configured in `app.py`:

```python
MODEL = "phi3:mini"
```

To switch models:

```python
MODEL = "gemma:2b"
# or
MODEL = "llama3.2:3b"
```

Model name must exactly match the output of:

```bash
ollama list
```

---

## Performance Notes

* First request may be slower due to model cold start
* Subsequent requests are significantly faster
* Best performance achieved by:

  * Keeping Ollama running in the background
  * Using smaller models (phi3 or gemma)
  * Avoiding excessive prompt verbosity

---

## Limitations

* No persistent conversation memory (stateless by default)
* Performance depends on local hardware
* Smaller models may struggle with very long structured outputs

---

## Planned Enhancements

* Persistent conversation memory
* Multi-session chat UI
* Model auto-selection (speed vs quality)
* Workout progression tracking
* Exportable workout plans (PDF / JSON)
* Desktop packaging (Electron or Tauri)

---

## Author

Built as a hands-on learning project focused on:

* Local LLM deployment
* FastAPI backend design
* Prompt engineering for structured outputs
* Offline AI application architecture

