from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import requests

app = FastAPI()

# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# CORS (frontend access)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request schema
class ChatRequest(BaseModel):
    message: str


# System prompt (optimized for speed + gym focus)
SYSTEM_PROMPT = """
Gym coach. Short answers. Bullet points only.
"""


@app.get("/", response_class=HTMLResponse)
def home():
    with open("templates/index.html", "r", encoding="utf-8") as f:
        return f.read()


@app.post("/chat")
def chat(req: ChatRequest):

    payload = {
        "model": "phi3:latest",
        "prompt": f"{SYSTEM_PROMPT}\nUser: {req.message}",
        "stream": False
    }

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json=payload,
            timeout=180
        )

        result = response.json()

        return {
            "response": result.get("response", "No response from model.")
        }

    except Exception as e:
        return {
            "response": f"Error: {str(e)}"
        }