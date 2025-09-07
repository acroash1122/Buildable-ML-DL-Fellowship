# import numpy as np
# import pandas as pd

# def add_gaussian_noise(df, column, mean=0, std=1):
#     """Add Gaussian noise to a numeric column."""
#     noisy = df[column] + np.random.normal(mean, std, size=len(df))
#     df[column + "_noisy"] = noisy
#     return df

# def oversample_rows(df, n=100):
#     """Oversample random rows from dataset."""
#     sampled = df.sample(n, replace=True)
#     return pd.concat([df, sampled], ignore_index=True)


# Question 7 addition:
# import numpy as np
# import pandas as pd

# def add_gaussian_noise(df, column, mean=0, std=1):
#     """Add Gaussian noise to a numeric column."""
#     noisy = df[column] + np.random.normal(mean, std, size=len(df))
#     df[column + "_noisy"] = noisy
#     return df

# def oversample_rows(df, n=100):
#     """Oversample random rows from dataset."""
#     sampled = df.sample(n, replace=True)
#     return pd.concat([df, sampled], ignore_index=True)

# def augment_dataset(df, noise_std=0.05):
#     """
#     Augment dataset by duplicating with Gaussian noise
#     to increase size at least 2x.
#     """
#     df_copy = df.copy()

#     # Add Gaussian noise to numeric columns
#     num_cols = df_copy.select_dtypes(include=[np.number]).columns
#     for col in num_cols:
#         noise = np.random.normal(0, noise_std * df_copy[col].std(), size=len(df_copy))
#         df_copy[col] = df_copy[col] + noise

#     # Concatenate original + noisy copy
#     augmented_df = pd.concat([df, df_copy], ignore_index=True)
#     return augmented_df


#Question 8 modification:
import numpy as np
import pandas as pd

def augment_dataset(df, noise_std=0.05, target_column="Purchased"):
    """
    Augment dataset by duplicating rows with Gaussian noise on numeric features
    (excluding the target column). Returns a dataset ~2x bigger.
    """
    df_copy = df.copy()

    # Add Gaussian noise only to numeric feature columns (excluding target)
    num_cols = df_copy.select_dtypes(include=[np.number]).columns
    if target_column in num_cols:
        num_cols = num_cols.drop(target_column)

    for col in num_cols:
        noise = np.random.normal(0, noise_std * df_copy[col].std(), size=len(df_copy))
        df_copy[col] = df_copy[col] + noise

    # Concatenate original + noisy copy
    augmented_df = pd.concat([df, df_copy], ignore_index=True)

    return augmented_df
