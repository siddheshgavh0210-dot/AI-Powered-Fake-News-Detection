import pandas as pd

from preprocess import clean_text

# Load datasets
fake_df = pd.read_csv("dataset/Fake.csv")
true_df = pd.read_csv("dataset/True.csv")

# Add labels
fake_df["label"] = 0
true_df["label"] = 1

# Merge datasets
data = pd.concat([fake_df, true_df], ignore_index=True)

# Shuffle dataset
data = data.sample(frac=1, random_state=42).reset_index(drop=True)

# Clean title and article text
data["title"] = data["title"].apply(clean_text)
data["text"] = data["text"].apply(clean_text)

print(data.head())

# Save cleaned dataset
data.to_csv("dataset/clean_news.csv", index=False)

print("\nClean dataset saved successfully!")
print(f"Total Records : {len(data)}")