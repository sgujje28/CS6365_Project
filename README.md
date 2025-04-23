
# StudyGenie - Study Resource Generator

## Overview
StudyGenie automates study material generation from lecture slides and notes.  
It extracts text from PDFs/images, summarizes key points, and generates flashcards to assist students in efficient studying.

## Features
- Extract text from PDFs and images using **Tesseract OCR**
- Summarize content using **Hugging Face BART model**
- Generate flashcards from extracted text using a **question-generation model**

## Installation
1. Install **Python 3.8+**
2. Install **Tesseract OCR**
   - **Linux/Mac**:  
     sudo apt install tesseract-ocr
   - **Windows**:  
     Download from https://github.com/tesseract-ocr/tesseract

3. Install Python packages:
   pip install fastapi uvicorn pytesseract pdf2image pillow transformers torch

## Running the Application
1. Start the FastAPI server:
   uvicorn main:app --reload

2. Open your browser and navigate to:
   http://127.0.0.1:8000

## API Endpoints
- Upload File: POST /upload/
- Extract Text: POST /extract_text/
- Summarize Text: POST /summarize_text/
- Generate Flashcards: POST /generate_flashcards/

## Project Structure
📂 StudyGenie
├── main.py
├── uploads/
├── templates/
│   └── index.html
├── static/
│   └── script.js
├── README.md

## License
MIT License
