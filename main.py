
from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
import os
import shutil
import pytesseract
from pdf2image import convert_from_path
from PIL import Image
from transformers import pipeline

app = FastAPI()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

summarizer = pipeline("summarization")
qa_pipeline = pipeline("question-generation")

@app.get("/", response_class=HTMLResponse)
def serve_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename, "path": file_path}

@app.post("/extract_text/")
async def extract_text(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = ""
    if file.filename.endswith(".pdf"):
        images = convert_from_path(file_path)
        for img in images:
            text += pytesseract.image_to_string(img) + "\n"
    elif file.filename.endswith((".png", ".jpg", ".jpeg")):
        image = Image.open(file_path)
        text = pytesseract.image_to_string(image)
    else:
        return {"error": "Unsupported file format"}

    return {"filename": file.filename, "extracted_text": text}

@app.post("/summarize_text/")
async def summarize_text(text: str):
    summary = summarizer(text, max_length=150, min_length=50, do_sample=False)
    return {"original_text": text, "summary": summary[0]['summary_text']}

@app.post("/generate_flashcards/")
async def generate_flashcards(text: str):
    try:
        questions = qa_pipeline(text)
        flashcards = [q['question'] for q in questions]
        return {"flashcards": flashcards}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
