🧠 CNN and ANN Implementation on MNIST and Cats vs Dogs Datasets
📘 Overview

This project demonstrates the implementation and comparison of Artificial Neural Networks (ANNs) and Convolutional Neural Networks (CNNs) for image classification tasks using two popular datasets:

MNIST Dataset – Handwritten digits classification (0–9).

Cats vs Dogs Dataset – Binary classification to distinguish between cat and dog images.

The goal is to analyze and compare the performance of ANN and CNN models, understand their architectural differences, and document the improvements achieved through convolutional feature extraction.

⚙️ Features

ANN and CNN implementation for both datasets

Data preprocessing, normalization, and augmentation

Use of EarlyStopping and ModelCheckpoint callbacks

Performance evaluation with accuracy/loss graphs

Model saving and loading from Google Drive (Colab)

Comparison tables and reflections included

📁 Project Structure
├── mnist_ann_cnn.ipynb          # Notebook for MNIST ANN + CNN comparison
├── cats_dogs_ann_cnn.ipynb      # Notebook for Cats vs Dogs ANN + CNN comparison
├── best_mnist_ann.h5            # Saved ANN model for MNIST
├── best_mnist_cnn.h5            # Saved CNN model for MNIST
├── best_cats_dogs_ann.h5        # Saved ANN model for Cats vs Dogs
├── best_cats_dogs_cnn.h5        # Saved CNN model for Cats vs Dogs
├── README.md                    # Project overview and usage guide
└── docs/
    ├── Month3_Week2_Assignment_Completed.docx   # Full assignment report

🚀 How to Run (Google Colab)
1️⃣ Clone the Repository
!git clone https://github.com/<your-username>/cnn-ann-comparison.git
%cd cnn-ann-comparison

2️⃣ Mount Google Drive
from google.colab import drive
drive.mount('/content/drive')

3️⃣ Install Dependencies

All required libraries are included with TensorFlow in Colab:

!pip install tensorflow matplotlib

4️⃣ Run MNIST Experiment

Open mnist_ann_cnn.ipynb in Colab.

Run all cells to:

Train an ANN on MNIST digits.

Train a CNN on MNIST digits.

Compare accuracy and loss.

5️⃣ Run Cats vs Dogs Experiment

Open cats_dogs_ann_cnn.ipynb in Colab.

Ensure dataset is stored in Google Drive under:

/content/drive/MyDrive/cats_and_dogs_filtered/


Run all cells to:

Train both ANN and CNN.

Observe performance improvement with CNN.

Save the best models in Drive.

📊 Results Summary
Dataset	Model	Accuracy	Observation
MNIST	ANN	~97%	Performs well but misses spatial context
MNIST	CNN	~99%	Captures spatial features → superior accuracy
Cats vs Dogs	ANN	~70–75%	Struggles with complex visual patterns
Cats vs Dogs	CNN	~85–90%	Excels at feature extraction and generalization
💡 Key Learnings

CNNs outperform ANNs in image classification tasks because they can extract spatial hierarchies using convolution and pooling layers.

ANNs are faster and simpler but lose critical spatial information after flattening images.

Proper data augmentation, callbacks, and dropout reduce overfitting and improve stability.

🧰 Technologies Used

Python 3

TensorFlow / Keras

Matplotlib

Google Colab

Google Drive (for model storage)

🧑‍💻 Author

Ahsan
Student Project — Month 3 Week 2 Assignment
📘 Course Focus: Deep Learning — Convolutional Neural Networks