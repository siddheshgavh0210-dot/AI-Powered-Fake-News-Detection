from flask import Flask, render_template, request
from utils.predictor import predict_news, compare_models
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    news = request.form["news"]
    model = request.form["model"]

    prediction, confidence = predict_news(news, model)
    comparison = compare_models(news)
    model_names = {
        "logistic": "Logistic Regression",
        "randomforest": "Random Forest",
        "knn": "K-Nearest Neighbors",
        "neural": "Neural Network"
    }
    

    return render_template(
    "result.html",
    prediction=prediction,
    confidence=confidence,
    model=model_names.get(model, model),
    article=news,
    comparison=comparison
)


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)