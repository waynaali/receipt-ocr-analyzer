# 🧾 OCR & Intelligent Document Processing System

### (Weeks 5–7 Integrated AI Pipeline Project)

An end-to-end **Document Intelligence System** that transforms unstructured document images into structured, machine-readable JSON using OCR, image processing, and NLP techniques.

It evolves across three stages:

* **Week 5 → OCR baseline system**
* **Week 6 → Image preprocessing + CNN digit recognition**
* **Week 7 → NLP-based information extraction + structured output**
* **Final → FastAPI deployment for real-time document classification**

---

# 📌 Project Overview

This system performs intelligent document understanding by combining:

* Optical Character Recognition (OCR)
* Image preprocessing (OpenCV)
* Machine Learning classification (TF-IDF + Logistic Regression)
* Rule-based extraction (Regex)
* NLP-based Named Entity Recognition (spaCy)
* REST API deployment (FastAPI)

---

# 🧩 System Pipeline

```text
Input Image
   ↓
Image Preprocessing (OpenCV)
   ↓
OCR (Tesseract)
   ↓
Text Cleaning & Feature Extraction
   ↓
ML Classification (Document Type)
   ↓
Information Extraction (Regex + spaCy NER)
   ↓
Structured JSON Output
```

---

# 📁 WEEK 5: BASIC OCR PIPELINE

## 🎯 Objectives

* Extract raw text from document images using OCR
* Understand limitations of unprocessed OCR output

## 🛠 Implementation

* `pytesseract.image_to_string()`
* PIL / OpenCV image loading

## 📊 Output

* Raw unstructured text extracted from:

  * invoices
  * resumes
  * memos

## ⚠️ Limitations

* Noise-sensitive OCR
* No structure in extracted text
* No entity recognition

---

# 🖼 WEEK 6: IMAGE PREPROCESSING + CNN DIGIT RECOGNITION

## 🎯 Objectives

* Improve OCR accuracy using preprocessing
* Train CNN model for digit classification

## 🔄 Image Preprocessing Techniques

* Grayscale conversion
* Thresholding
* Noise removal
* Morphological operations (erosion, dilation)
* Deskewing correction

## 🤖 CNN Model (MNIST Dataset)

### Architecture:

* Convolution layers
* ReLU activation
* MaxPooling
* Fully connected layers
* Softmax output (digits 0–9)

### Performance:

* Accuracy: ~99%
* Optimized for digit recognition tasks

---

# 🧠 WEEK 7: NLP + INFORMATION EXTRACTION

## 🎯 Objectives

* Extract structured data from OCR text
* Apply NLP for entity recognition
* Generate structured JSON output

---

## 🔍 Regex-Based Extraction

* Dates (multiple formats supported)
* Currency values
* Invoice numbers
* Reference IDs

---

## 🧠 spaCy NER Extraction

Entities extracted:

* PERSON
* ORG (Organizations)
* GPE (Locations)
* DATE
* MONEY

---

## 📦 FINAL OUTPUT (STRUCTURED JSON)

```json
{
  "document_type": "invoice",
  "invoice_number": "INV-2024-001",
  "dates": ["March 15, 2024"],
  "amounts": [1250.50],
  "persons": ["John Smith"],
  "organizations": ["Acme Corporation"],
  "locations": ["New York"],
  "total_amount": 1250.50,
  "confidence": 0.71
}
```

---

# ⚡ FASTAPI DEPLOYMENT

## 🚀 Endpoints

### 1. Classify Document

```
POST /classify
```

### 2. Extract Information

```
POST /extract
```

### 3. Full Pipeline

```
POST /process
```

---

## 🌐 Run Server

```bash
py -m uvicorn api:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

---

# 🛠 TECHNOLOGIES USED

### OCR & Vision

* Tesseract OCR
* OpenCV
* PIL

### Machine Learning

* Scikit-learn (TF-IDF, Logistic Regression)
* TensorFlow / Keras (CNN)

### NLP

* spaCy
* Regex (Python re)

### Backend

* FastAPI
* Uvicorn

---

# 🚀 REAL-WORLD APPLICATIONS

* Invoice automation systems
* Financial document processing
* Receipt digitization
* Banking document analysis
* Enterprise document intelligence systems

---

# 🔮 FUTURE IMPROVEMENTS

* Transformer-based OCR (TrOCR)
* Table structure extraction
* End-to-end deep learning pipeline
* Cloud deployment (AWS / Render / HuggingFace)
* Web UI dashboard for uploads

---

# 👨‍💻 AUTHOR

**Wayna Ali**
BS Electronics 
Introduction To AI Project
Document Intelligence System (OCR + ML + NLP)

---

# ⭐ FINAL NOTE

This project demonstrates a **complete AI pipeline from raw images to structured intelligence**, combining:

> Computer Vision + Machine Learning + Natural Language Processing + API Deployment


