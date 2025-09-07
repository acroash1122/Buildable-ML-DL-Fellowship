import os
import numpy as np
import pandas as pd
import random
import datetime

class InvalidFilePathError(Exception):
    """Raised when the file path is invalid."""
    pass

class DataGenerationError(Exception):
    """Raised when dataset generation fails due to wrong parameters."""
    pass


class DataGenerator:
    def __init__(self, n_rows=500, save_path="Buildable-ML-DL-Fellowship/week3/synthetic_data_pipeline_project/data/raw/generated_data.csv", seed=None):
        self.n_rows = n_rows
        self.save_path = save_path
        if seed is not None:
            random.seed(seed)
            np.random.seed(seed)

    def log_error(self, message):
        """Log errors to logs/errors.txt"""
        os.makedirs("logs", exist_ok=True)
        with open("logs/errors.txt", "a") as f:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"[{timestamp}] {message}\n")

    def generate_numeric_features(self):
        if self.n_rows <= 0: 
            raise DataGenerationError("Number of rows must be greater than zero.")
        age = np.random.randint(18, 70, self.n_rows)
        income = np.random.randint(20000, 150000, self.n_rows)
        score = np.random.randint(0, 100, self.n_rows)
        years_of_experience = np.random.randint(0, 40, self.n_rows)
        purchases_last_year = np.random.randint(0, 50, self.n_rows)
        return age, income, score, years_of_experience, purchases_last_year

    def generate_categorical_features(self):
        gender = np.random.choice(["Male", "Female", "Other"], self.n_rows, p=[0.48, 0.48, 0.04])
        product_type = np.random.choice(["Electronics", "Clothing", "Food", "Books"], self.n_rows)
        return gender, product_type

    def generate_target(self, income, score):
        probs = (income / income.max()) * 0.5 + (score / 100) * 0.5
        purchase = np.random.binomial(1, probs)
        return purchase

    def generate_dataset(self):
        try:
            age, income, score, exp, purchases = self.generate_numeric_features()
            gender, product = self.generate_categorical_features()
            purchase = self.generate_target(income, score)

            data = pd.DataFrame({
                "Age": age,
                "Income": income,
                "Score": score,
                "Experience": exp,
                "Purchases_Last_Year": purchases,
                "Gender": gender,
                "Product_Type": product,
                "Purchased": purchase
            })
            return data
        except DataGenerationError as e:
            self.log_error(str(e))
            raise

    def save_dataset(self, data):
        try:
            # Validate path
            folder = os.path.dirname(self.save_path)
            if folder and not os.path.exists(folder):
                raise InvalidFilePathError(f"Invalid path: {self.save_path}")

            data.to_csv(self.save_path, index=False)
            print(f"Dataset saved to {self.save_path}")

        except InvalidFilePathError as e:
            self.log_error(str(e))
            raise

        except Exception as e:
            self.log_error(f"Unexpected error while saving dataset: {str(e)}")
            raise

    def run(self):
        try:
            data = self.generate_dataset()
            self.save_dataset(data)
            return data
        except Exception as e:
            print(f"[ERROR] {str(e)}")
            return None

 # invalid folder
if __name__ == "__main__":

    generator = DataGenerator(
        n_rows=500,
        save_path=r"C:\invalid_path\generated_data.csv", 
        seed=42
    )

    df = generator.run()

