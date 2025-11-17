from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from google import genai

app = FastAPI()

client = genai.Client()  # auto reads GEMINI_API_KEY


@app.get("/api")
def idea():
    stream = client.models.generate_content(
        model="gemini-1.5-flash",       # FAST free model
        contents="Come up with a new business idea for AI Agents",
        stream=True                     # STREAM ENABLED
    )

    def event_stream():
        for chunk in stream:
            text = chunk.text or ""
            if text:
                for line in text.split("\n"):
                    yield f"data: {line}\n"
                yield "\n"

    return StreamingResponse(event_stream(), media_type="text/event-stream")
