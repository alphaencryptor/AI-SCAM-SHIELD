import joblib


# Load trained model
model = joblib.load("scam_model.pkl")


def predict_scam(text):

    if not text or not text.strip():
        return "safe", 0.0

    # Prediction
    prediction = model.predict([text])[0]

    # Probability
    probabilities = model.predict_proba([text])[0]

    classes = model.classes_

    scam_probability = 0.0

    for class_name, probability in zip(
        classes,
        probabilities
    ):
        if class_name == "scam":
            scam_probability = probability

    scam_probability = round(
        scam_probability * 100,
        2
    )

    return prediction, scam_probability


# --------------------------------
# TEST
# --------------------------------

if __name__ == "__main__":

    test_message = (
        "Your bank account will be blocked. "
        "Verify your KYC immediately and enter OTP."
    )

    prediction, probability = predict_scam(
        test_message
    )

    print("--------------------------------")
    print("       ML SCAM DETECTOR")
    print("--------------------------------")

    print("Prediction:", prediction)
    print("Scam Probability:", probability, "%")