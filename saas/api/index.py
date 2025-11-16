from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from google import genai
import os

app = FastAPI()

# Create Gemini client (auto reads GEMINI_API_KEY from environment)
client = genai.Client()

@app.get("/api", response_class=PlainTextResponse)
def idea():
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Come up with a new business idea for AI Agents",
    )

    return response.text
