from pathlib import Path

import edge_tts
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="AI Content Factory - TTS Service",
    version="1.0.0"
)

OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)


class VoiceRequest(BaseModel):
    text: str
    voice: str = "en-US-AriaNeural"
    filename: str = "voice.mp3"


@app.get("/")
async def root():
    return {
        "status": "ok",
        "service": "tts-service"
    }


@app.post("/generate-voice")
async def generate_voice(request: VoiceRequest):

    output_file = OUTPUT_DIR / request.filename

    communicate = edge_tts.Communicate(
        text=request.text,
        voice=request.voice
    )

    await communicate.save(str(output_file))

    return {
        "status": "success",
        "file": str(output_file.resolve()),
        "voice": request.voice
    }