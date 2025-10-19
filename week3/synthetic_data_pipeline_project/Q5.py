import pandas as pd
import numpy as np
import os

raw_path = "Buildable-ML-DL-Fellowship/week3/synthetic_data_pipeline_project/data/raw/generated_data.csv"  
df = pd.read_csv(raw_path)

print(" Raw dataset sample:")
print(df.head())

for col in ["Age", "Income", "Gender"]:
    df.loc[df.sample(frac=0.01).index, col] = np.nan

print(" With NaNs inserted:")
print(df.head(10))


num_cols = df.select_dtypes(include=[np.number]).columns
for col in num_cols:
    df[col].fillna(df[col].median(), inplace=True)

cat_cols = df.select_dtypes(exclude=[np.number]).columns
for col in cat_cols:
    df[col].fillna(df[col].mode()[0], inplace=True)

print(" After handling NaNs:")
print(df.head(10))

df_encoded = pd.get_dummies(df, columns=["Gender", "Product_Type"], drop_first=True)

print(" Encoded dataset sample:")
print(df_encoded.head())

os.makedirs("Buildable-ML-DL-Fellowship/week3/synthetic_data_pipeline_project/data/processed", exist_ok=True)

processed_path = "Buildable-ML-DL-Fellowship/week3/synthetic_data_pipeline_project/data/processed/cleaned_data.csv"
df_encoded.to_csv(processed_path, index=False)

print(f" Cleaned dataset saved to {processed_path}")
