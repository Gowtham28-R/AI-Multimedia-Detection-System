# AI Multimedia Detection System

## Overview

AI Multimedia Detection System is a Computer Vision and Machine Learning project designed to distinguish between real and AI-generated multimedia content. The system analyzes images and videos using advanced feature extraction techniques and machine learning models to provide accurate classification results.

The project combines DINOv2 visual representations with a LightGBM classifier and provides an interactive web-based interface for real-time predictions.

---

## Features

- Real vs AI-generated image classification
- Real vs AI-generated video classification
- DINOv2-based feature extraction
- LightGBM classification model
- Confidence score visualization
- Sample frame analysis for videos
- Interactive Gradio web application
- Modular and scalable architecture

---

## System Architecture

Dataset
↓
Frame Extraction & Preprocessing
↓
Feature Extraction (DINOv2)
↓
Feature Vector Generation
↓
LightGBM Classification
↓
Prediction & Confidence Score
↓
Gradio Web Interface

---

## Technologies Used

### Programming Language
- Python 3.10

### Machine Learning
- LightGBM
- Scikit-Learn

### Deep Learning
- PyTorch
- DINOv2

### Computer Vision
- OpenCV
- Pillow

### Web Interface
- Gradio

### Data Processing
- NumPy
- Pandas

---

## Project Structure

```text
AI-Multimedia-Detection-System/
│
├── README.md
├── requirements.txt
│
├── extract_frames.py
├── extract_frames_cv2.py
├── split_into_train_img.py
├── remove_duplicate_images.py
│
├── extract_dinov2_features.py
├── extract_features.py
├── feature_extraction_image.py
│
├── train_lightgbm_model.py
├── image_classifier.py
├── predict.py
│
├── video_app.py
│
└── lightgbm_model.pkl

## Results
- High accuracy real vs AI media detection
- Efficient feature extraction pipeline
- Real-time web-based prediction system
- Lightweight deployment architecture

## Future Improvements
- Deepfake-specific detection
- Multi-class AI generator identification
- Audio authenticity verification
- Cloud deployment support
- Real-time webcam moderation

## Author

Gowtham Kumar
Artificial Intelligence And Data Science

## Interested in:

- Artificial Intelligence
- Computer Vision
- Machine Learning
- Deep Learning
- Multimedia Forensics
