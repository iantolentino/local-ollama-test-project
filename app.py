from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "mistral:latest"  

app = FastAPI(title="Ollama Web Chat")

class PromptRequest(BaseModel):
    prompt: str


@app.get("/", response_class=HTMLResponse)
def index():
    return """
<!DOCTYPE html>
<html>
<head>
    <title>Local Ollama Chat</title>
    <style>
        body { font-family: Arial; max-width: 800px; margin: auto; }
        textarea { width: 100%; height: 100px; }
        button { padding: 10px 20px; margin-top: 10px; }
        #response { white-space: pre-wrap; margin-top: 20px; }
    </style>
</head>
<body>
    <h2>Local Ollama Chat</h2>
    <textarea id="prompt" placeholder="Ask something..."></textarea><br>
    <button onclick="send()">Send</button>
    <div id="response"></div>

    <script>
        async function send() {
            const prompt = document.getElementById("prompt").value;

            const res = await fetch("/chat", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ prompt: prompt })
            });

            const data = await res.json();
            document.getElementById("response").innerText =
                data.response || data.error || "No response";
        }
    </script>
</body>
</html>
"""


@app.post("/chat")
def chat(request: PromptRequest):
    payload = {
        "model": MODEL_NAME,
        "prompt": f"""
You are a fitness-only AI assistant.
Only answer questions related to workouts, gym training,
nutrition, recovery, and injury prevention.

User question:
{request.prompt}
""",
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)

    if response.status_code != 200:
        return {"error": response.text}

    return {"response": response.json().get("response", "")}