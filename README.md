# 🧾 OCR & Digit Recognition System

An advanced **Document Intelligence project** that performs **image preprocessing, perspective correction, deskewing, morphological processing, and digit recognition using a Convolutional Neural Network (CNN)**.

This project extends the basic OCR system by improving input image quality and integrating a deep learning model for handwritten digit classification.

---

# 📌 Project Overview

This project demonstrates how **image preprocessing techniques combined with deep learning** can significantly improve text and digit recognition from images.

The system processes raw images using several enhancement steps and then applies a **CNN-based model trained on the MNIST dataset** to recognize handwritten digits.

It is part of **AI Lab – Week 6: Image Preprocessing and CNN-based Digit Recognition**.

---

# 🎯 Objectives

* Perform **perspective correction** on distorted document images
* Implement **automatic deskewing** for proper alignment
* Apply **morphological image processing techniques**
* Train a **CNN model for handwritten digit recognition**
* Achieve **high classification accuracy using MNIST dataset**
* Visualize **training performance and predictions**

---

# 🔄 System Workflow

Image Input
→ Perspective Correction
→ Deskewing
→ Morphological Processing
→ CNN Feature Extraction
→ Digit Classification
→ Results Visualization

---

# 🖼 Image Preprocessing Techniques

## 1️⃣ Perspective Correction

Used to correct **tilted or distorted images** using perspective transformation.

This ensures the document appears **flat and properly aligned** before further processing.

---

## 2️⃣ Automatic Deskewing

Automatically detects the **skew angle** of the image and rotates it to align text or digits horizontally.

This improves OCR and recognition accuracy.

---

## 3️⃣ Morphological Operations

Several morphological image processing techniques were implemented:

**Erosion**

* Removes small noise
* Shrinks objects

**Dilation**

* Expands objects
* Fills small gaps

**Opening**

* Erosion followed by dilation
* Removes small noise while preserving object shape

**Closing**

* Dilation followed by erosion
* Fills small holes in objects

---

# 🤖 CNN Model for Digit Recognition

A **Convolutional Neural Network (CNN)** was implemented for handwritten digit classification.

### Architecture Summary

Input Layer
28×28 grayscale images

Convolution Layer
Extracts spatial features

Activation Function
ReLU

Pooling Layer
MaxPooling

Flatten Layer
Converts feature maps to vector

Dense Layers
Fully connected layers for classification

Output Layer
Softmax activation for **10 digit classes (0–9)**

---

# 📊 Model Training

Dataset: **MNIST Handwritten Digits**

Training parameters:

Optimizer: Adam
Loss Function: Categorical Crossentropy
Batch Size: 128
Epochs: 10
Validation Split: 10%

---

# 📈 Training Visualization

The following graphs were generated:

* **Training vs Validation Accuracy**
* **Training vs Validation Loss**

These plots verify **model convergence and learning performance**.

---

# 🔍 Test Predictions

The trained model was evaluated on the **MNIST test dataset**.

Predictions were visualized to confirm:

* Correct digit classifications
* Occasional misclassifications for analysis

---

# ✅ Key Achievements

✔ Perspective correction successfully implemented
✔ Automatic deskewing working correctly
✔ All morphological operations demonstrated
✔ CNN model designed and trained
✔ Achieved **~99% accuracy on MNIST dataset**
✔ Training history visualized using plots
✔ Test predictions successfully displayed

---

# 🛠 Technologies Used

* Python
* OpenCV
* NumPy
* Matplotlib
* TensorFlow / Keras
* Scikit-learn

---

# 📁 Project Structure

ocr-digit-recognition/

images/
notebook.ipynb
preprocessing.py
cnn_model.py
README.md

---

# 🚀 Applications

* OCR-based document digitization
* Automated form processing
* Bank cheque recognition
* Receipt and invoice processing
* Handwritten digit recognition systems

---

# 🔮 Future Improvements

* Extend system to **full text OCR recognition**
* Integrate **CNN + LSTM models for sequence recognition**
* Deploy system as **web application**
* Improve robustness for **noisy real-world images**

---

# 👨‍💻 Author

Wayna Ali
BS Electronics Student
AI Lab – Week 6 Project

