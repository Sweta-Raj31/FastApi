import json
import requests
import uuid
import os
from fastapi import FastAPI, File, UploadFile, HTTPException
from PyPDF2 import PdfReader
from .celery import celery_app

app = FastAPI()

# Directory to temporarily store uploaded PDF files
temp_dir = "app/tmp/pdf_uploads"
if not os.path.exists(temp_dir):
    os.makedirs(temp_dir)

# Celery task to process PDF
@celery_app.task
def process_pdf(url: str, pdf_id: str, file_path: str):
    text = extract_text_from_pdf(file_path)
    response = {"pdf_id": pdf_id, "text": text}
    requests.post(url, json=response)
    os.remove(file_path)

# Function to extract text from a PDF file
def extract_text_from_pdf(file_path: str) -> str:
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

# Function to save the uploaded PDF file temporarily
def save_pdf(file: UploadFile):
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)

    file_extension = file.filename.split(".")[-1]
    if file_extension.lower() != "pdf":
        raise HTTPException(status_code=400, detail="File format not supported.")

    pdf_id = str(uuid.uuid4())
    file_path = os.path.join(temp_dir, f"{pdf_id}.pdf")
    with open(file_path, "wb") as f:
        f.write(file.file.read())

    return pdf_id, file_path

# Dictionary to store the processing status
processing_status = {}
# Global variable to store the current pdf_id
current_pdf_id = None

# Webhook endpoint to upload PDF files
@app.post("/webhook/")
async def upload_pdf(file: UploadFile = File(...)):
    global current_pdf_id
    try:
        pdf_id, file_path = save_pdf(file)
        current_pdf_id = pdf_id  # Update the global variable
        processing_status[pdf_id] = "processing"
        text = extract_text_from_pdf(file_path)
        os.remove(file_path)
        data = {'pdf_id': pdf_id, 'text': text}
        # Send the data to the webhook
        webhook_url = 'https://webhook.site/cdbb1b50-031c-4901-8429-a1c88d10767a'
        r = requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
        processing_status[pdf_id] = "completed"
        return {"pdf_id": pdf_id, "text": text}
    except Exception as e:
        print(f"Error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

# Polling endpoint to check the status of PDF processing
@app.post("/polling/")
async def polling():
    global current_pdf_id
    if current_pdf_id is None:
        raise HTTPException(status_code=404, detail="No PDF is currently being processed")

    pdf_id = current_pdf_id
    if pdf_id not in processing_status:
        raise HTTPException(status_code=404, detail="PDF ID not found")

    status = processing_status[pdf_id]
    if status == "processing":
        raise HTTPException(status_code=202, detail="File is processing, please wait.")
    elif status == "completed":
        return {"pdf_id": pdf_id, "status": "completed"}
    else:
        raise HTTPException(status_code=500, detail=status)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
