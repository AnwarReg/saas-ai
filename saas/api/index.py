from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from google import genai
import os

app = FastAPI()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

@app.get("/api")
def idea():
    prompt = "Come up with a new business idea for AI Agents"

    def event_stream():
        stream = client.models.generate_content_stream(
            model="gemini-2.0-flash-exp",   # <-- FIXED MODEL
            contents=prompt
        )
        
        for chunk in stream:
            if chunk.text:
                for line in chunk.text.split("\n"):
                    yield f"data: {line}\n"
                yield "\n"

    return StreamingResponse(event_stream(), media_type="text/event-stream")
