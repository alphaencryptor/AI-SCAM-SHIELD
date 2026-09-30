import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score


# --------------------------------
# LOAD DATASET
# --------------------------------

data = pd.read_csv("training_data.csv")

X = data["text"]
y = data["label"]


# --------------------------------
# TRAIN / TEST SPLIT
# --------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# --------------------------------
# CREATE ML PIPELINE
# --------------------------------

model = Pipeline([
    (
        "tfidf",
        TfidfVectorizer(
            lowercase=True,
            ngram_range=(1, 2)
        )
    ),
    (
        "classifier",
        LogisticRegression(
            max_iter=1000
        )
    )
])


# --------------------------------
# TRAIN MODEL
# --------------------------------

model.fit(X_train, y_train)


# --------------------------------
# TEST MODEL
# --------------------------------

predictions = model.predict(X_test)

accuracy = accuracy_score(
    y_test,
    predictions
)

print("--------------------------------")
print("      AI SCAMSHIELD ML MODEL")
print("--------------------------------")

print("Model Accuracy:", round(accuracy * 100, 2), "%")


# --------------------------------
# SAVE MODEL
# --------------------------------

joblib.dump(
    model,
    "scam_model.pkl"
)

print("Model saved as: scam_model.pkl")