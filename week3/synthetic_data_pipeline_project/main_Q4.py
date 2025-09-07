from synthetic_data.data_generator import DataGenerator
from synthetic_data import stats, augment, visuals

# Step 1: Generate dataset
generator = DataGenerator(
    n_rows=500,
    save_path="Buildable-ML-DL-Fellowship/week3/synthetic_data_pipeline_project/data/raw/generated_data.csv",
    seed=42
)
df = generator.run()

# Step 2: Use stats module
print("Mean Age:", stats.mean(df["Age"]))
print("Median Income:", stats.median(df["Income"]))
print("Std Dev of Score:", stats.std(df["Score"]))

# Step 3: Use augment module
df_aug = augment.add_gaussian_noise(df, "Income", mean=0, std=5000)
df_aug = augment.oversample_rows(df_aug, n=50)

# Step 4: Use visuals module
visuals.plot_histogram(df_aug, "Age")
visuals.plot_scatter(df_aug, "Income_noisy", "Score")


