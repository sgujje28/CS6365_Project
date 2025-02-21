StudyGenie - Study Resource Generator

Overview:
StudyGenie automates study material generation from lecture slides and notes. It extracts text from PDFs/images, summarizes key points, and generates flashcards.

Features:

- Extract text using Tesseract OCR
- Summarize content using Hugging Face BART
- Generate flashcards from extracted text

Installation:

- Install Python 3.8+
- Install Tesseract OCR
- Run: pip install fastapi uvicorn pytesseract pdf2image pillow transformers torch

Running:

- Start server: uvicorn main:app --reload

API Endpoints:

- Upload File: POST /upload/
- Extract Text: POST /extract_text/
- Summarize Text: POST /summarize_text/
- Generate Flashcards: POST /generate_flashcards/

Project Structure:

- main.py (Backend)
- uploads/ (Storage)
- README.md (Documentation)

Future Enhancements:

- Web UI
- Support more file formats
- Improved AI models
