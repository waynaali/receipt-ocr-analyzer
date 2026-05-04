# 🧾 OCR & Intelligent Document Processing System

### (Weeks 5 + 6 + 7 Combined Project)

An end-to-end **Document Intelligence system** that evolves from basic OCR to advanced AI-based information extraction using:

* OCR (Tesseract)
* Image preprocessing (OpenCV)
* CNN-based digit recognition
* Regex-based structured extraction
* spaCy Named Entity Recognition (NER)
* JSON-based structured output pipeline

---

# 📌 Project Overview

This project demonstrates a complete progression of document understanding:

* **Week 5 → Basic OCR pipeline**
* **Week 6 → Image enhancement + CNN digit recognition**
* **Week 7 → Information extraction + NLP-based structuring**

The final system converts unstructured document images into **clean structured JSON data**.

---

# 🧩 WEEK 5: BASIC OCR PIPELINE

## 🎯 Objectives

* Introduce OCR using Tesseract
* Extract raw text from images
* Basic image loading and preprocessing
* Understand limitations of raw OCR output

---

## 🔍 Key Work Done

### 1️⃣ OCR using Tesseract

* Converted image → text
* Used `pytesseract.image_to_string()`

### 2️⃣ Image Handling

* Loaded images using PIL / OpenCV
* Converted images into readable format for OCR

### 3️⃣ Basic Output

Extracted raw text such as:

* Invoice content
* Dates (unstructured)
* Amounts (no formatting)

---

## ⚠️ Limitations Identified

* No noise removal
* Skewed images reduce accuracy
* Unstructured output
* No entity understanding

---

# 🖼 WEEK 6: IMAGE PREPROCESSING + CNN DIGIT RECOGNITION

## 🎯 Objectives

* Improve OCR input quality
* Apply image preprocessing techniques
* Train CNN for digit recognition (MNIST)

---

## 🔄 Image Preprocessing Pipeline

* Perspective Correction
* Automatic Deskewing
* Morphological Operations:

  * Erosion
  * Dilation
  * Opening
  * Closing

---

## 🤖 CNN Model (MNIST)

### Architecture:

* Input: 28×28 grayscale images
* Convolution layers
* ReLU activation
* MaxPooling
* Dense layers
* Softmax output (0–9 digits)

### Training:

* Optimizer: Adam
* Loss: Categorical Crossentropy
* Epochs: 10
* Accuracy: ~99%

---

## 📊 Results

* Clean digit recognition
* Strong generalization on MNIST dataset
* Improved OCR readiness

---

# 🧠 WEEK 7: INFORMATION EXTRACTION + NER

## 🎯 Objectives

* Extract structured data from OCR text
* Use Regex for pattern extraction
* Apply spaCy NER
* Build complete invoice pipeline
* Export JSON output

---

## 🔍 Regex-Based Extraction

### ✔ Dates

Supports:

* MM/DD/YYYY
* DD-MM-YYYY
* Month DD, YYYY
* YYYY-MM-DD

### ✔ Currency Amounts

Handles:

* $1,250.50
* 1250.50
* $1250

### ✔ Invoice Numbers

Formats:

* INV-2024-001
* ORDER-ABC123
* #12345

---

## 🧠 Named Entity Recognition (spaCy)

Extracted:

* PERSON → names
* ORG → organizations
* GPE/LOC → locations
* DATE → time references
* MONEY → financial values

---

## 🔗 Final Pipeline

Image → OCR → Regex → NER → Structuring → JSON

---

## 📦 Final Output Example

```json id="wk7json"
{
  "invoice_number": "INV-2024-001",
  "dates": ["March 15, 2024"],
  "amounts": [1250.50, 125.05],
  "persons": ["John Smith"],
  "organizations": ["Acme Corporation"],
  "locations": ["New York"],
  "total_amount": 1250.50,
  "invoice_date": "March 15, 2024"
}
```

---

# 📊 Visualization

* spaCy displaCy entity highlighting
* HTML export (`entities.html`)
* Color-coded named entities

---

# 🛠 TECHNOLOGIES USED

### Week 5:

* Tesseract OCR
* PIL / OpenCV

### Week 6:

* OpenCV
* TensorFlow / Keras
* NumPy
* Matplotlib

### Week 7:

* Regex (`re`)
* spaCy NLP
* JSON processing
* pytesseract

---

# 🚀 APPLICATIONS

* Invoice automation systems
* Financial document processing
* Bank cheque recognition
* Receipt digitization
* AI document understanding systems

---

# 🔮 FUTURE IMPROVEMENTS

* Transformer-based OCR (TrOCR)
* Table structure extraction
* Web-based OCR dashboard
* Cloud deployment (API system)
* Multilingual document support

---

# 👨‍💻 AUTHOR

**Wayna Ali**
BS Electronics
AI Lab Project 2
OCR + CNN + NLP Document Intelligence System

✔ Or make a **professional PDF report (submission-ready formatting)**
✔ Or help you **merge your notebooks into a clean final project repo structure**
