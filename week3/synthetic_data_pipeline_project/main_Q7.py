from synthetic_data import stats, augment
import pandas as pd
import os

df = pd.read_csv("Buildable-ML-DL-Fellowship/week3/synthetic_data_pipeline_project/data/processed/cleaned_data.csv")

print("Age -> Mean:", stats.mean(df["Age"]))
print("Age -> Median:", stats.median(df["Age"]))
print("Age -> Std Dev:", stats.std(df["Age"]))

print("Income -> Mean:", stats.mean(df["Income"]))
print("Income -> Median:", stats.median(df["Income"]))
print("Income -> Std Dev:", stats.std(df["Income"]))


# Augment dataset (2x size)
df_aug = augment.augment_dataset(df, noise_std=0.05, target_column="Purchased")

# Save augmented dataset
os.makedirs("Buildable-ML-DL-Fellowship/week3/synthetic_data_pipeline_project/data/processed", exist_ok=True)
augmented_path = "Buildable-ML-DL-Fellowship/week3/synthetic_data_pipeline_project/data/processed/augmented_data.csv"
df_aug.to_csv(augmented_path, index=False)

print(f"[OK] Augmented dataset saved to {augmented_path}")
print("Original size:", df.shape[0])
print("Augmented size:", df_aug.shape[0])
