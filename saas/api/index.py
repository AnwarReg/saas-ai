from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import google.genai as genai
import os

app = FastAPI()

@app.get("/api", response_class=PlainTextResponse)
def idea():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return "ERROR: GEMINI_API_KEY missing"

    client = genai.Client(api_key=api_key)

    prompt = "Come up with a new business idea for AI Agents."

    response = client.models.generate(
        model="gemini-2.0-flash",
        prompt=prompt
    )

    return response.text
