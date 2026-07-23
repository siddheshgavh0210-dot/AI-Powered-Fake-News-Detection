import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier

from sklearn.metrics import accuracy_score, classification_report

# ==========================
# Load Dataset
# ==========================

df = pd.read_csv("dataset/clean_news.csv")

# Combine title and text into one feature
df["content"] = (
    df["title"].fillna("").astype(str) + " " +
    df["text"].fillna("").astype(str)
)

X = df["content"]
y = df["label"]
# ==========================
# TF-IDF
# ==========================

vectorizer = TfidfVectorizer(
    max_features=5000,
    stop_words="english"
)

X = vectorizer.fit_transform(X)

# ==========================
# Train Test Split
# ==========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ==========================
# Models
# ==========================

models = {

    "logistic_regression": LogisticRegression(max_iter=1000),

    "knn": KNeighborsClassifier(n_neighbors=5),

    "random_forest": RandomForestClassifier(
        n_estimators=200,
        random_state=42
    ),

    "neural_network": MLPClassifier(
        hidden_layer_sizes=(128,64),
        max_iter=300,
        random_state=42
    )

}

# ==========================
# Create Models Folder
# ==========================

os.makedirs("models", exist_ok=True)

# Save Vectorizer

joblib.dump(
    vectorizer,
    "models/tfidf_vectorizer.pkl"
)

print("\n==============================")

print("Training Models")

print("==============================\n")

results=[]

for name, model in models.items():

    print(f"Training {name}...")

    model.fit(X_train, y_train)

    predictions=model.predict(X_test)

    accuracy=accuracy_score(
        y_test,
        predictions
    )

    print(f"Accuracy : {accuracy*100:.2f}%")

    print(classification_report(
        y_test,
        predictions
    ))

    joblib.dump(
        model,
        f"models/{name}.pkl"
    )

    results.append(
        [name,accuracy]
    )

print("\n==============================")

print("Training Complete")

print("==============================")

print("\nModel Comparison\n")

results=sorted(
    results,
    key=lambda x:x[1],
    reverse=True
)

for model,acc in results:

    print(f"{model:25} {acc*100:.2f}%")

print("\nAll models saved successfully.")