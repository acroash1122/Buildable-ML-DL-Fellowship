from synthetic_data.data_generator import DataGenerator
from synthetic_data import visuals
import pandas as pd


df = pd.read_csv("Buildable-ML-DL-Fellowship/week3/synthetic_data_pipeline_project/data/processed/cleaned_data.csv")


visuals.plot_histogram(df, "Age", save_path="Buildable-ML-DL-Fellowship/week3/synthetic_data_pipeline_project/plots/age_histogram.png")
visuals.plot_bar(df, "Gender_Male", save_path="Buildable-ML-DL-Fellowship/week3/synthetic_data_pipeline_project/plots/gender_bar.png")  
visuals.plot_correlation_heatmap(df, save_path="Buildable-ML-DL-Fellowship/week3/synthetic_data_pipeline_project/plots/correlation_heatmap.png")
visuals.plot_scatter(df, "Income", "Score", save_path="Buildable-ML-DL-Fellowship/week3/synthetic_data_pipeline_project/plots/income_vs_score.png")

print("[OK] Plots saved in plots/ folder")
