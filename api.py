from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from PIL import Image
import pytesseract
import joblib
import io

# Initialize FastAPI
app = FastAPI(
    title="Document Intelligence API",
    description="OCR, Classification, and Extraction",
    version="1.0.0"
)

# Load models

vectorizer = joblib.load("vectorizer.pkl")
classifier = joblib.load("classifier.pkl")

@app.get("/")
def root():
    return {
        "message": "Document Intelligence API",
        "version": "1.0.0",
        "endpoints": ["/classify", "/extract", "/process"]
    } 
from fastapi import UploadFile, File
from fastapi.responses import JSONResponse
from PIL import Image
import io

@app.post("/classify")
async def classify_document(file: UploadFile = File(...)):
    """
    Classify document type
    Returns: document type and confidence
    """
    try:
        # Read image
        contents = await file.read()
        image = Image.open(io.BytesIO(contents))

        # OCR
        text = pytesseract.image_to_string(image)

        # Vectorize and classify
        text_vec = vectorizer.transform([text])
        prediction = classifier.predict(text_vec)[0]
        probabilities = classifier.predict_proba(text_vec)[0]
        confidence = max(probabilities)

        return {
            "document_type": prediction,
            "confidence": float(confidence),
            "all_probabilities": {
                cls: float(prob)
                for cls, prob in zip(classifier.classes_, probabilities)
            }
        }

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": str(e)}
        )
import sys
import io
from fastapi import UploadFile, File
from fastapi.responses import JSONResponse
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# Import extraction functions from Week 7
sys.path.append("../")
def extract_dates(text):
    return []

def extract_amounts(text):
    return []

def extract_entities(text):
    return []
@app.post("/extract")
async def extract_information(file: UploadFile = File(...)):
    """
    Extract information from document
    Returns: extracted dates, amounts, entities
    """
    try:
        # Read and OCR
        contents = await file.read()
        image = Image.open(io.BytesIO(contents))
        text = pytesseract.image_to_string(image)

        # Extract information
        dates = extract_dates(text)
        amounts = extract_amounts(text)
        entities = extract_entities(text)

        return {
            "dates": dates,
            "amounts": amounts,
            "entities": entities,
            "raw_text": text[:500]
        }

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": str(e)}
        )
from fastapi import UploadFile, File
from fastapi.responses import JSONResponse
from PIL import Image
import io

@app.post("/process")
async def process_document(file: UploadFile = File(...)):
    """
    Complete pipeline: OCR + Classify + Extract
    Returns: document type and extracted data
    """
    try:
        # Read and OCR
        contents = await file.read()
        image = Image.open(io.BytesIO(contents))
        text = pytesseract.image_to_string(image)

        # Classify
        text_vec = vectorizer.transform([text])
        doc_type = classifier.predict(text_vec)[0]
        confidence = max(classifier.predict_proba(text_vec)[0])

        # Extract
        extracted_data = {
            "dates": extract_dates(text),
            "amounts": extract_amounts(text),
            "entities": extract_entities(text)
        }

        return {
            "document_type": doc_type,
            "confidence": float(confidence),
            "extracted_data": extracted_data,
            "status": "success"
        }

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": str(e), "status": "failed"}
        )