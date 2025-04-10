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
     ```bash
     sudo apt install tesseract-ocr
     ```
   - **Windows**:  
     Download from [Tesseract GitHub](https://github.com/tesseract-ocr/tesseract)

3. Install Python packages:
   ```bash
   pip install fastapi uvicorn pytesseract pdf2image pillow transformers torch
   ```

## Running the Application

1. Start the FastAPI server:

   ```bash
   uvicorn main:app --reload
   ```

2. Open your browser and navigate to:
   ```
   http://127.0.0.1:8000
   ```

## API Endpoints

- **Upload File**: `POST /upload/`  
  Upload PDFs or images

- **Extract Text**: `POST /extract_text/`  
  Extract text from uploaded files

- **Summarize Text**: `POST /summarize_text/`  
  Generate a summary from extracted text

- **Generate Flashcards**: `POST /generate_flashcards/`  
  Generate flashcards from text

## Project Structure

```
📂 StudyGenie
├── 📄 main.py          # FastAPI Backend
├── 📂 uploads          # Uploaded files directory
├── 📂 templates/
│   └── index.html      # UI for uploading files and viewing output
├── 📂 static/
│   └── script.js       # JS to connect frontend to API
├── 📄 README.md        # Project documentation
```

## Future Enhancements

- Develop a **Web UI** for user-friendly interactions (✔ in progress)
- Support additional file formats (Word, Markdown, etc.)
- Improve AI models for more accurate summarization & flashcard generation
- Implement **database support** for storing and retrieving user-generated study materials

## License

MIT License
