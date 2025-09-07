import random
import numpy as np
import pandas as pd
import os

class DataGenerator:
    def __init__(self, n_rows=500, save_path="Buildable-ML-DL-Fellowship/week3/synthetic_data_pipeline_project/data/raw/generated_data.csv", seed=None):  
        self.n_rows = n_rows
        self.save_path = save_path
        if seed is not None:
            random.seed(seed)
            np.random.seed(seed)

    def generate_numeric_features(self):
        """Generate numerical features such as age, income, etc."""
        age = np.random.randint(18, 70, self.n_rows)                   
        income = np.random.randint(20000, 150000, self.n_rows)        
        score = np.random.randint(0, 100, self.n_rows)                 
        years_of_experience = np.random.randint(0, 40, self.n_rows)    
        purchases_last_year = np.random.randint(0, 50, self.n_rows)   
        return age, income, score, years_of_experience, purchases_last_year

    def generate_categorical_features(self):
        """Generate categorical features such as gender, product type, etc."""
        gender = np.random.choice(["Male", "Female", "Other"], self.n_rows, p=[0.48, 0.48, 0.04])
        product_type = np.random.choice(["Electronics", "Clothing", "Food", "Books"], self.n_rows)
        return gender, product_type

    def generate_target(self, income, score):
        """Generate a binary target (classification)."""
     
        probs = (income / income.max()) * 0.5 + (score / 100) * 0.5
        purchase = np.random.binomial(1, probs)
        return purchase

    def generate_dataset(self):
        """Generate the entire dataset and return as a DataFrame."""
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

    def save_dataset(self, data):
        """Save dataset to CSV."""
        os.makedirs(os.path.dirname(self.save_path), exist_ok=True)
        data.to_csv(self.save_path, index=False)
        print(f" Dataset saved to {self.save_path}")

    def run(self):
        """Generate and save dataset in one go."""
        data = self.generate_dataset()
        self.save_dataset(data)
        return data


if __name__ == "__main__":
    generator = DataGenerator(n_rows=500, save_path="Buildable-ML-DL-Fellowship/week3/synthetic_data_pipeline_project/data/raw/generated_data.csv", seed=42)
    df = generator.run()
    print(df.head())
