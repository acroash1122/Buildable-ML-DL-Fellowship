from synthetic_data.model_trainer import ModelTrainer

# Train on cleaned dataset
trainer_clean = ModelTrainer(data_path="Buildable-ML-DL-Fellowship/week3/synthetic_data_pipeline_project/data/processed/cleaned_data.csv", target_column="Purchased")
results_clean = trainer_clean.train_and_evaluate()
print("Results on Cleaned Dataset:\n", results_clean)

# Bonus: Train on augmented dataset
trainer_aug = ModelTrainer(data_path="Buildable-ML-DL-Fellowship/week3/synthetic_data_pipeline_project/data/processed/augmented_data.csv", target_column="Purchased")
results_aug = trainer_aug.train_and_evaluate()
print("Results on Augmented Dataset:\n", results_aug)
