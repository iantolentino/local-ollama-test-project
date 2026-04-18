from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import requests
import json

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str


# MODEL OPTIONS
MODEL = "phi3:mini"
# MODEL = "gemma:2b"
# MODEL = "llama3.2:3b"


SYSTEM_PROMPT = """
You are a professional certified gym coach.

ABSOLUTE RULES:
- If the user asks for X days, output ALL X days.
- NEVER stop early.
- NEVER summarize.
- NEVER say "this would continue".
- Output Day 1 through Day X explicitly.
- No emojis.
- No blog language.
- No filler.

FORMAT (MANDATORY):

Day X
- Exercise — Sets x Reps | Rest
  Reason: short practical benefit (max 10 words)

Do not include warm-up or cool-down unless asked.
Keep reasons concise.
"""


@app.get("/", response_class=HTMLResponse)
def home():
    with open("templates/index.html", "r", encoding="utf-8") as f:
        return f.read()


@app.post("/chat")
def chat(req: ChatRequest):

    def stream():
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": MODEL,
                "prompt": f"""
{SYSTEM_PROMPT}

USER REQUEST:
{req.message}

IMPORTANT:
Count days carefully.
Do not stop until ALL days are complete.
""",
                "stream": True,
                "options": {
                    "temperature": 0.6,
                    "top_p": 0.9,
                    "num_predict": 1200
                }
            },
            stream=True,
            timeout=300
        )

        for line in response.iter_lines():
            if line:
                data = json.loads(line.decode("utf-8"))
                if "response" in data:
                    yield data["response"]

    return StreamingResponse(stream(), media_type="text/plain")