import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing.image import load_img, img_to_array

class DiseaseDetector:
    def __init__(self, model_path=r"D:\Final Project\Buildable-ML-DL-Fellowship\Final_project\models\disease_cnn.h5"):
        self.model = tf.keras.models.load_model(model_path)
        self.target_size = (224, 224)

    def predict(self, image_path):
        img = load_img(image_path, target_size=self.target_size)
        arr = img_to_array(img)
        arr = np.expand_dims(arr, axis=0) / 255.0

        pred = self.model.predict(arr)
        class_index = pred.argmax(axis=1)[0]

        # Retrieve class names dynamically
        class_labels = list(self.model.class_names) if hasattr(self.model, 'class_names') else None

        if class_labels:
            return class_labels[class_index]
        return int(class_index)
