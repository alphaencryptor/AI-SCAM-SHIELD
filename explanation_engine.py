# AI ScamShield
# Explanation Engine


def generate_explanation(
    detected_keywords,
    url_indicators,
    ml_prediction=None,
    ml_probability=None
):

    explanations = []

    # --------------------------------
    # MESSAGE INDICATORS
    # --------------------------------

    keywords = [
        str(keyword).lower()
        for keyword in detected_keywords
    ]

    if "urgent" in keywords:
        explanations.append(
            "🚨 Urgency manipulation detected. "
            "The message is pressuring you to act quickly."
        )

    if "immediately" in keywords:
        explanations.append(
            "⏱️ Immediate-action language detected."
        )

    if "kyc" in keywords:
        explanations.append(
            "🔐 KYC verification request detected."
        )

    if "otp" in keywords:
        explanations.append(
            "🔑 OTP-related content detected. "
            "Never share an OTP with another person."
        )

    if "password" in keywords:
        explanations.append(
            "🔑 Password-related request detected."
        )

    if "bank" in keywords:
        explanations.append(
            "🏦 Banking or financial content detected."
        )

    if "blocked" in keywords:
        explanations.append(
            "⚠️ Account-blocking threat detected."
        )

    if "payment" in keywords:
        explanations.append(
            "💳 Payment-related request detected."
        )

    if "reward" in keywords or "prize" in keywords:
        explanations.append(
            "🎁 Reward or prize-related content detected."
        )

    if "click" in keywords:
        explanations.append(
            "🖱️ The message asks you to click a link."
        )


    # --------------------------------
    # URL INDICATORS
    # --------------------------------

    for indicator in url_indicators:

        indicator_text = str(indicator).lower()

        if "ip address" in indicator_text:
            explanations.append(
                "🌐 The URL uses an IP address instead "
                "of a normal domain."
            )

        elif "very long url" in indicator_text:
            explanations.append(
                "📏 The URL is unusually long."
            )

        elif "suspicious keyword" in indicator_text:
            explanations.append(
                f"🔎 {indicator}"
            )

        elif "suspicious-looking domain" in indicator_text:
            explanations.append(
                f"🌐 {indicator}"
            )

        elif "@ symbol" in indicator_text:
            explanations.append(
                "⚠️ The URL contains an @ symbol."
            )

        elif "many subdomains" in indicator_text:
            explanations.append(
                "🌐 The URL contains an unusually large "
                "number of subdomains."
            )

        elif "hyphen" in indicator_text:
            explanations.append(
                "🔎 The domain contains a hyphen, "
                "which can be a suspicious indicator."
            )

        elif "does not use https" in indicator_text:
            explanations.append(
                "🔓 The URL does not use HTTPS."
            )


    # --------------------------------
    # ML EXPLANATION
    # --------------------------------

    if (
        ml_prediction == "scam"
        and ml_probability is not None
    ):

        explanations.append(
            f"🤖 The machine-learning model classified "
            f"the text as potentially fraudulent "
            f"with a {ml_probability}% scam probability."
        )


    # --------------------------------
    # REMOVE DUPLICATES
    # --------------------------------

    explanations = list(
        dict.fromkeys(explanations)
    )


    # --------------------------------
    # DEFAULT MESSAGE
    # --------------------------------

    if not explanations:

        explanations.append(
            "ℹ️ No major suspicious indicators were "
            "identified by the current prototype."
        )


    return explanations



if __name__ == "__main__":

    explanations = generate_explanation(
        detected_keywords=[
            "urgent",
            "kyc",
            "otp",
            "bank",
            "blocked"
        ],
        url_indicators=[
            "Suspicious keyword: kyc",
            "Suspicious-looking domain ending: .xyz"
        ],
        ml_prediction="scam",
        ml_probability=91.5
    )

    print("--------------------------------")
    print("     SCAM EXPLANATION ENGINE")
    print("--------------------------------")

    for explanation in explanations:
        print("-", explanation)