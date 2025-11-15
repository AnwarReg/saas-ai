from fastapi import FastAPI  # type: ignore
from fastapi.responses import PlainTextResponse  # type: ignore
import google.generativeai as genai  # type: ignore
import os  # type: ignore

app = FastAPI()

# Create a Gemini client (free model = "gemini-1.5-flash")
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

@app.get("/api", response_class=PlainTextResponse)
def idea():
    prompt = "Come up with a new business idea for AI Agents"

    model = genai.GenerativeModel("gemini-1.5-flash")  # free model
    response = model.generate_content(prompt)

    return response.text
