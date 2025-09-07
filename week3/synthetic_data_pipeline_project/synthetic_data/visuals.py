import matplotlib.pyplot as plt
import seaborn as sns
import os

def plot_histogram(df, column, save_path="plots/histogram.png"):
    os.makedirs("plots", exist_ok=True)
    plt.figure(figsize=(6,4))
    plt.hist(df[column], bins=20, color="skyblue", edgecolor="black")
    plt.title(f"Histogram of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.savefig(save_path)
    plt.close()

def plot_bar(df, column, save_path="plots/barplot.png"):
    os.makedirs("plots", exist_ok=True)
    plt.figure(figsize=(6,4))
    df[column].value_counts().plot(kind="bar", color="lightgreen", edgecolor="black")
    plt.title(f"Bar plot of {column}")
    plt.xlabel(column)
    plt.ylabel("Count")
    plt.savefig(save_path)
    plt.close()

def plot_correlation_heatmap(df, save_path="plots/correlation_heatmap.png"):
    os.makedirs("plots", exist_ok=True)
    plt.figure(figsize=(8,6))
    corr = df.corr(numeric_only=True)
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Heatmap of Numerical Features")
    plt.savefig(save_path)
    plt.close()

def plot_scatter(df, col1, col2, save_path="plots/scatter.png"):
    os.makedirs("plots", exist_ok=True)
    plt.figure(figsize=(6,4))
    plt.scatter(df[col1], df[col2], alpha=0.5, color="orange")
    plt.title(f"Scatter plot: {col1} vs {col2}")
    plt.xlabel(col1)
    plt.ylabel(col2)
    plt.savefig(save_path)
    plt.close()
