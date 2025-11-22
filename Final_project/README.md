# Smart Farming System Using ML & DL

## Overview
The **Smart Farming System** is an AI-based application designed to assist farmers in making data-driven decisions for crop management. It integrates **crop recommendation**, **disease detection**, and an intelligent **smart agent** to optimize agricultural productivity.

---

## Features
- **Crop Predictor**: Recommends the best crop based on soil nutrients, environmental conditions, and climate data.
- **Disease Detector**: Detects plant diseases from leaf images using a CNN model.
- **Smart Farming Agent**: Combines all modules to provide automated recommendations for crop and disease management.
- **RAG QA Tool** (Optional): Answer agricultural queries based on embedded knowledge.

---

## System Components

### Crop Predictor
- **Input Parameters**: N, P, K, Temperature, Humidity, pH, Rainfall, Soil Fertility, Climate Index.
- **Output**: Recommended crop.
- **Model**: Random Forest / Decision Tree.
- **Libraries**: `scikit-learn`, `joblib`, `numpy`.

### Disease Detector
- **Input**: Leaf image.
- **Output**: Disease classification.
- **Model**: CNN trained using TensorFlow/Keras.
- **Libraries**: `tensorflow`, `keras`, `h5py`.

### Smart Farming Agent
- Integrates Crop Predictor and Disease Detector.
- Provides a unified interface for farmer recommendations.

---

## Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
Navigate to project folder:

bash
Copy code
cd Final_project/src
Install required packages:

bash
Copy code
pip install -r requirements.txt
Requirements include:

nginx
Copy code
tensorflow
keras
numpy
scikit-learn
joblib
h5py
Pillow
opencv-python
sentence-transformers
faiss-cpu
Usage
Crop Prediction
python
Copy code
from crop_predictor import CropPredictor

features = {
    'N': 90, 'P': 42, 'K': 43,
    'temperature': 25, 'humidity': 80,
    'ph': 6.5, 'rainfall': 200,
    'soil_fertility': 7, 'climate_index': 0.85
}

crop_tool = CropPredictor()
recommended_crop = crop_tool.predict(features)
print("Recommended Crop:", recommended_crop)
Disease Detection
python
Copy code
from disease_detector import DiseaseDetector

disease_tool = DiseaseDetector()
result = disease_tool.predict("path_to_leaf_image.jpg")
print("Detected Disease:", result)
Smart Farming Agent
python
Copy code
from smart_agent import SmartFarmingAgent

agent = SmartFarmingAgent()
# Use agent.crop_tool or agent.disease_tool for predictions
Project Structure
css
Copy code
src/
 ├─ crop_predictor.py
 ├─ disease_detector.py
 ├─ smart_agent.py
 ├─ test_agent.py
models/
 ├─ crop_model.pkl
 ├─ scaler.joblib
 ├─ label_encoder.joblib
 ├─ disease_cnn.h5
notebooks/
 ├─ crop_recommendation_notebook
 ├─ disease_detection_notebook
README.md
Challenges
Loading legacy .h5 models trained on Colab locally.

Ensuring Python package versions compatibility.

Organizing project modules for smooth imports.

Future Work
Add more crop types and diseases.

Integrate IoT sensor data for real-time predictions.

Develop web or mobile interface for farmers.

