from pathlib import Path
from typing import List

from fastapi import FastAPI
from pydantic import BaseModel
import subprocess

app = FastAPI(
    title = "AI Content Factory - Video Service",
    version = "1.0.0"
)

OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)

class Overlay(BaseModel):
    start: int
    end: int
    text: str

class VideoRequest(BaseModel):
    image_path: str
    voice_path: str
    output_file: str = "output.mp4"
    overlays: List[Overlay]

@app.get("/")
async def root():
    return {
        "status": "ok",
        "service": "video-service"
    }

def build_drawtext_filter(overlays: List[Overlay]) -> str:
    filters = []

    for overlay in overlays:
        text = (
            overlay.text
            .replace(":", "\\:")
            .replace("'", "\\'")
        )

        filters.append(
            (
                f"drawtext="
                f"text='{text}':"
                f"fontcolor=white:"
                f"fontsize=34:"
                f"box=1:"
                f"boxcolor=black@0.5:"
                f"boxborderw=8:"
                f"x=(w-text_w)/2:"
                f"y=h-180:"
                f"enable='between(t,{overlay.start},{overlay.end})'"
            )
        )

    return ",".join(filters)

@app.post("/generate-video")
async def generate_video(request: VideoRequest):

    output_path = OUTPUT_DIR / request.output_file

    filter_string = build_drawtext_filter(request.overlays)

    command = [
        "ffmpeg",
        "-y",
        "-loop", "1",
        "-i", request.image_path,
        "-i", request.voice_path,
        "-vf", filter_string,
        "-c:v", "libx264",
        "-tune", "stillimage",
        "-c:a", "aac",
        "-b:a", "192k",
        "-shortest",
        "-pix_fmt", "yuv420p",
        str(output_path)
    ]

    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        return {
            "status": "error",
            "message": result.stderr
        }

    return {
        "status": "success",
        "output_file": str(output_path)
    }