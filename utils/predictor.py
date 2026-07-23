import joblib
from preprocessing.preprocess import clean_text

vectorizer = joblib.load("models/tfidf_vectorizer.pkl")

MODELS = {
    "logistic": "models/logistic_regression.pkl",
    "randomforest": "models/random_forest.pkl",
    "knn": "models/knn.pkl",
    "neural": "models/neural_network.pkl"
}
MODEL_NAMES = {
    "logistic": "Logistic Regression",
    "randomforest": "Random Forest",
    "knn": "K-Nearest Neighbors (KNN)",
    "neural": "Neural Network"
}
def compare_models(news_text):
    cleaned_text = clean_text(news_text)
    vector = vectorizer.transform([cleaned_text])

    results = []

    for key, path in MODELS.items():
        model = joblib.load(path)

        prediction = model.predict(vector)[0]

        label = "REAL NEWS" if prediction == 1 else "FAKE NEWS"

        confidence = 100.0
        if hasattr(model, "predict_proba"):
            confidence = round(max(model.predict_proba(vector)[0]) * 100, 2)

        results.append({
    "model": MODEL_NAMES[key],
    "prediction": label,
    "confidence": confidence
    })
    return results

def predict_news(news_text, model_name):

    model = joblib.load(MODELS[model_name])

    # Clean the user input
    cleaned_text = clean_text(news_text)

    # TF-IDF
    vector = vectorizer.transform([cleaned_text])

    prediction = model.predict(vector)[0]

    confidence = 100.0

    if hasattr(model, "predict_proba"):
        probabilities = model.predict_proba(vector)[0]
        confidence = round(max(probabilities) * 100, 2)

    print("Original:", news_text)
    print("Cleaned:", cleaned_text)
    print("Prediction:", prediction)
    print("Confidence:", confidence)

    label = "REAL NEWS" if prediction == 1 else "FAKE NEWS"

    return label, confidence