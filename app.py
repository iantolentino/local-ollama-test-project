from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import requests

app = FastAPI()

# serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")


# allow frontend calls
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str


@app.get("/", response_class=HTMLResponse)
def home():
    with open("templates/index.html", "r", encoding="utf-8") as f:
        return f.read()


@app.post("/chat")
def chat(req: ChatRequest):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "mistral:latest",
            "prompt": f"You are a gym coach AI. Answer clearly and concisely.\nUser: {req.message}",
            "stream": False
        }
    )

    return {"response": response.json()["response"]}