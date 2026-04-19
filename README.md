# 🧾 Receipt OCR Analyzer

A Document Intelligence project that extracts and analyzes text from receipt images using Tesseract OCR and EasyOCR, with OpenCV preprocessing and Regex-based data extraction.

---

## 📌 Project Overview

This project demonstrates how OCR (Optical Character Recognition) is used to extract information from receipt images.  
It is part of **Lab 5: Document Intelligence - OCR Basics**.

Extracted data includes:
- Merchant Name  
- Date  
- Items  
- Prices  
- Total Amount  

---

## ⚙️ Features

- Image-based text extraction  
- OCR using Tesseract and EasyOCR  
- Image preprocessing using OpenCV  
- OCR comparison  
- Receipt parsing using Regex  
- Multiple receipt support  

---

## 🔄 Workflow

Image → Preprocessing → OCR → Text Extraction → Data Parsing

---

## 🛠️ Technologies Used

- Python  
- Tesseract OCR  
- EasyOCR  
- OpenCV  
- Pillow  
- Regex  
- Matplotlib  

---

## 🚀 How It Works

1. Load image  
2. Preprocess image (grayscale, blur, threshold)  
3. Apply OCR  
4. Compare outputs  
5. Extract structured data  

---

## 📊 Example Output

COFFEE SHOP  
Cappuccino $4.50  
Croissant $3.25  
TOTAL: $7.75  

---

## 🎯 Objective

To understand OCR systems and improve text extraction accuracy using image preprocessing techniques.

---

## 📁 Project Structure

receipt-ocr-analyzer/

- images/
- receipts/
- notebook.ipynb
- main.py
- README.md

---

## 👨‍💻 Author

Wayna Ali  
BS Electronics Student  
AI Lab 5 Project
