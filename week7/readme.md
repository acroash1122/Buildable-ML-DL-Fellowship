Predicting Airbnb Listing Success (Albany, NY)
Objective

This case study analyzes Airbnb listings in Albany, NY to predict:

Price (Regression)

Popularity (Classification)

and to explore the impact of host, property, and location factors on listing success.

Part A: Git & GitHub Workflow

Created feature branches from the main repository buildables/:

week7-assignment

week7-regression-classification

week7-deeplearning

Each branch handled distinct tasks (EDA/ML/DL).

Used regular commits and pull requests (PRs) for merges.

Maintained screenshots for:

Branch creation

Commit history

PR merges into main

Part B: Case Study Tasks

1. Data Loading & Cleaning

Dataset: Inside Airbnb – Albany, NY (listings.csv), 459 rows × 79 columns
Steps performed:

Removed high-missing and irrelevant columns (neighborhood_overview, host_about, etc.)

Converted price and percentage fields to numeric

Parsed host_since as datetime

Filled numeric columns with median, categorical with mode

Final dataset: 72 columns, 0 missing values

2. Exploratory Data Analysis (EDA)

Key Visualizations:

Histogram of price → right-skewed (most listings under $200)

Boxplot of room_type vs price → Entire homes are most expensive

Scatter: price vs number_of_reviews → lower prices attract more reviews

Correlation heatmap → price correlated with accommodates, bedrooms, bathrooms

Geospatial scatter (lat/long vs price) → higher prices near central Albany

Summary:

Price distribution is right-skewed, and location, property type, and room type are major price influencers.

3. Feature Engineering

Engineered four new predictive features:

Feature Description
host_tenure_days Days since host joined Airbnb
num_amenities Count of amenities listed
distance_from_center_km Haversine distance from Albany city center
desc_length Number of words in the listing description

All features showed realistic distributions and correlations.

4. Regression Modeling (Predict Price)

Models Trained:

Linear Regression

Random Forest Regressor

XGBoost Regressor

Model MAE RMSE R²
Linear Regression 34.19 57.58 0.409
Random Forest 33.43 72.09 0.074
XGBoost 37.92 96.97 -0.676

Applying log transformation on price improved results:

MAE = 28.88, RMSE = 55.67, R² = 0.45

✅ Linear Regression (log-transformed) chosen as final regression model.

5. Classification Modeling (Predict Popularity)

Target:
Listings with number_of_reviews > median = popular (1), else not popular (0).

Models:

Logistic Regression

Random Forest Classifier

Model Accuracy F1 ROC-AUC
Logistic Regression 0.76 0.74 0.85
Random Forest 0.82 0.80 0.90

✅ Best Model: Random Forest Classifier

False negatives (missing truly popular listings) are more costly than false positives (over-promoting average listings).

6. Deep Learning Experiment

Built a Keras Sequential model (MLP):

Input → Dense(128, relu) → Dropout(0.2) → Dense(64, relu) → Dense(1)

Results:

MAE = 36.11, RMSE = 59.47, R² = 0.37
Stable training (no overfitting), but smaller dataset limited performance.

✅ Classical Linear Regression outperformed the neural model for this dataset size.

Conclusions
Goal Best Model Key Insight
Price Prediction Linear Regression (log-transformed) Price mostly driven by room type, amenities, and host experience
Popularity Prediction Random Forest Classifier Popular listings tend to be affordable, well-equipped, and closer to city center

Business Takeaways:

Encourage new hosts to enhance amenities and write detailed descriptions.

Promote well-rated budget listings near city center to improve visibility.

Deep learning could be revisited with richer datasets (text + images).

✅ Deliverables Checklist

week7/ folder in repo

Git branches and PR screenshots

Cleaned dataset and EDA notebook

Regression + Classification models

Neural network experiment

Final report (this document)
