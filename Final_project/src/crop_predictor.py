import joblib
import numpy as np

class CropPredictor:
    def __init__(self, 
                 model_path=r"D:\Final Project\Buildable-ML-DL-Fellowship\Final_project\models1\crop_model.pkl",
                 scaler_path=r"D:\Final Project\Buildable-ML-DL-Fellowship\Final_project\models1\scaler.joblib",
                 label_path=r"D:\Final Project\Buildable-ML-DL-Fellowship\Final_project\models1\label_encoder.joblib"):

        self.model = joblib.load(model_path)
        self.scaler = joblib.load(scaler_path)
        self.label_encoder = joblib.load(label_path)

    def predict(self, features: dict):
        """
        features = {
            'N': value,
            'P': value,
            'K': value,
            'temperature': value,
            'humidity': value,
            'ph': value,
            'rainfall': value,
            'soil_fertility': value,
            'climate_index': value
        }
        """
        values = np.array([list(features.values())])
        scaled = self.scaler.transform(values)
        pred = self.model.predict(scaled)[0]
        crop = self.label_encoder.inverse_transform([pred])[0]
        return crop
