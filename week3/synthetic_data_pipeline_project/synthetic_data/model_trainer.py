import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
import joblib

class ModelTrainer:
    def __init__(self, data_path, target_column="Purchased"):
        self.data_path = data_path
        self.target_column = target_column
        self.models = {
            "LogisticRegression": LogisticRegression(max_iter=1000, solver="liblinear"),
            "RandomForest": RandomForestClassifier(n_estimators=100, random_state=42)
        }
        self.results = {}

    def load_data(self):
     df = pd.read_csv(self.data_path)
    
     # Force target column to be binary integers
     if self.target_column in df.columns:
        df[self.target_column] = df[self.target_column].round().astype(int)

     X = df.drop(columns=[self.target_column])
     y = df[self.target_column]

     return X, y



    def split_data(self, X, y, test_size=0.2, random_state=42):
        return train_test_split(X, y, test_size=test_size, random_state=random_state)

    def evaluate_model(self, model, X_test, y_test):
        y_pred = model.predict(X_test)
        y_proba = model.predict_proba(X_test)[:, 1] if hasattr(model, "predict_proba") else y_pred

        metrics = {
            "Accuracy": accuracy_score(y_test, y_pred),
            "Precision": precision_score(y_test, y_pred),
            "Recall": recall_score(y_test, y_pred),
            "F1-Score": f1_score(y_test, y_pred),
            "ROC-AUC": roc_auc_score(y_test, y_proba)
        }
        return metrics

    def train_and_evaluate(self):
        X, y = self.load_data()
        X_train, X_test, y_train, y_test = self.split_data(X, y)

        os.makedirs("models", exist_ok=True)
        os.makedirs("results", exist_ok=True)

        for name, model in self.models.items():
            model.fit(X_train, y_train)
            metrics = self.evaluate_model(model, X_test, y_test)

            self.results[name] = metrics

            # Save model
            joblib.dump(model, f"models/{name}.joblib")

        # Save metrics to CSV
        metrics_df = pd.DataFrame(self.results).T
        metrics_df.to_csv("results/metrics.csv")

        return self.results
