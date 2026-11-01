# AI Content Factory

## Overview

AI Content Factory is a personal project that explores AI-powered content creation and workflow automation.

The goal is to transform a simple technology topic into a publishable short-form video through a combination of AI models, workflow orchestration, image generation, voice synthesis, and multimedia processing.

This project serves as a hands-on learning platform for:

- AI Automation
- Workflow Design
- n8n
- Local LLMs
- Prompt Engineering
- Image Generation
- Video Assembly
- Personal Branding

---

## Vision

Build an automated content factory that turns ideas into short-form technology content.

```text
Topic
 ↓
AI Analysis
 ↓
Content Generation
 ↓
Media Creation
 ↓
Video Assembly
 ↓
Review & Approval
 ↓
TikTok Publishing
```

## Current Status

### Completed

- ✅ Docker environment setup
- ✅ n8n workflow implementation
- ✅ Ollama integration
- ✅ Qwen content generation
- ✅ Structured JSON responses
- ✅ AI image prompt generation
- ✅ ComfyUI installation
- ✅ DreamShaper image model setup
- ✅ First AI-generated image
- ✅ ComfyUI API workflow export

### In Progress

- ⏳ n8n → ComfyUI API integration
- ⏳ Image asset management
- ⏳ OneDrive integration

### Planned

- 📌 Text-to-Speech generation
- 📌 Video generation with FFmpeg
- 📌 Automatic publishing workflow
- 📌 TikTok API integration

## Repository Structure

```text
AI-Content-Factory
│
├── workflows
│   ├── n8n-content-generator.json
│   └── Generate-Image-from-Prompt.json
│
├── generated-images
│
├── docs
│
└── README.md
```

## Current Working Workflow

```text
User Topic
      ↓
Qwen
      ↓
Structured Content
      ↓
Image Prompt
      ↓
ComfyUI
      ↓
DreamShaper
      ↓
Generated Image
```

## Development Log

### Day 1

- Setup Docker
- Install n8n
- Configure Ollama
- Create Content Generation Workflow
- Install ComfyUI
- Configure DreamShaper
- Generate first AI image

## Current Technology Stack

- Docker
- n8n
- Ollama
- Qwen 2.5 7B
- ComfyUI
- DreamShaper
- GitHub Copilot

## Planned Technologies

- Edge-TTS
- FFmpeg
- OneDrive Integration
- TikTok API