# AI ScamShield
# Multilingual Scam Detector
# English + Hindi + Hinglish


# --------------------------------
# ENGLISH SUSPICIOUS WORDS
# --------------------------------

SUSPICIOUS_WORDS = [
    "urgent",
    "verify",
    "verification",
    "otp",
    "kyc",
    "blocked",
    "block",
    "account",
    "click",
    "payment",
    "reward",
    "prize",
    "winner",
    "refund",
    "bank",
    "upi",
    "password",
    "immediately",
    "claim",
    "login"
]


# --------------------------------
# HINDI + HINGLISH WORDS
# --------------------------------

HINDI_HINGLISH_WORDS = [

    # Hindi
    "तुरंत",
    "केवाईसी",
    "ओटीपी",
    "बैंक",
    "खाता",
    "बंद",
    "पासवर्ड",
    "इनाम",
    "पुरस्कार",
    "पैसे",
    "भुगतान",
    "सत्यापित",
    "सत्यापन",
    "लिंक",
    "क्लिक",

    # Hinglish
    "turant",
    "verify karo",
    "verify kare",
    "kyc karo",
    "kyc verify",
    "account block",
    "account band",
    "bank account",
    "otp do",
    "otp bhejo",
    "password do",
    "link kholo",
    "link open karo",
    "click karo",
    "payment karo",
    "paise bhejo",
    "paise do",
    "inaam",
    "cashback",
    "lottery"
]


# --------------------------------
# SCAM DETECTOR FUNCTION
# --------------------------------

def analyze_message(message):

    score = 0
    detected_keywords = []

    # Convert message to lowercase
    text = message.lower()


    # --------------------------------
    # ENGLISH DETECTION
    # --------------------------------

    for word in SUSPICIOUS_WORDS:

        if word.lower() in text:

            score += 8
            detected_keywords.append(word)


    # --------------------------------
    # HINDI / HINGLISH DETECTION
    # --------------------------------

    for word in HINDI_HINGLISH_WORDS:

        if word.lower() in text:

            score += 10
            detected_keywords.append(word)


    # --------------------------------
    # REMOVE DUPLICATES
    # --------------------------------

    detected_keywords = list(
        dict.fromkeys(detected_keywords)
    )


    # --------------------------------
    # LIMIT SCORE
    # --------------------------------

    score = min(score, 100)


    # --------------------------------
    # RISK LEVEL
    # --------------------------------

    if score >= 75:

        risk_level = "CRITICAL"

    elif score >= 50:

        risk_level = "HIGH"

    elif score >= 25:

        risk_level = "MEDIUM"

    else:

        risk_level = "LOW"


    return score, risk_level, detected_keywords


# --------------------------------
# TEST THE DETECTOR
# --------------------------------

if __name__ == "__main__":

    test_message = (
        "Aapka bank account block ho jayega. "
        "Turant KYC verify karo aur OTP bhejo."
    )

    score, risk_level, detected_keywords = analyze_message(
        test_message
    )

    print("--------------------------------")
    print("       AI SCAMSHIELD")
    print("--------------------------------")

    print("Message:")
    print(test_message)

    print()
    print("Risk Score:", score, "/100")
    print("Risk Level:", risk_level)

    print()
    print("Detected Indicators:")

    for keyword in detected_keywords:
        print("-", keyword)