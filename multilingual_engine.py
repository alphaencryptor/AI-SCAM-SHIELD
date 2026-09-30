from langdetect import detect, LangDetectException


def detect_language(text):

    if not text or not text.strip():
        return "unknown"

    try:
        language = detect(text)

        language_names = {
            "en": "English",
            "hi": "Hindi",
            "mr": "Marathi",
            "bn": "Bengali",
            "ta": "Tamil",
            "te": "Telugu",
            "gu": "Gujarati",
            "pa": "Punjabi",
            "kn": "Kannada",
            "ml": "Malayalam"
        }

        return language_names.get(
            language,
            language.upper()
        )

    except LangDetectException:
        return "Unknown"


if __name__ == "__main__":

    tests = [
        "Your bank account will be blocked immediately.",
        "आपका बैंक अकाउंट बंद हो जाएगा।",
        "Apka bank account block ho jayega."
    ]

    for text in tests:

        language = detect_language(text)

        print("--------------------------------")
        print("Text:", text)
        print("Detected Language:", language)