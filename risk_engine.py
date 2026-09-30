# AI ScamShield - Combined Risk Engine


def calculate_final_risk(message_score, url_score, has_url=False):
    """
    Combine message and URL scores into one final risk score.
    """

    # -----------------------------------
    # If both message and URL are present
    # -----------------------------------

    if has_url:

        final_score = (
            (message_score * 0.60)
            +
            (url_score * 0.40)
        )

    # -----------------------------------
    # If only message is present
    # -----------------------------------

    else:

        final_score = message_score


    # Convert to integer
    final_score = round(final_score)


    # Make sure score stays between 0 and 100
    final_score = max(0, min(final_score, 100))


    # -----------------------------------
    # Determine Risk Level
    # -----------------------------------

    if final_score <= 20:

        risk_level = "LOW"

    elif final_score <= 50:

        risk_level = "MEDIUM"

    elif final_score <= 75:

        risk_level = "HIGH"

    else:

        risk_level = "CRITICAL"


    return final_score, risk_level



if __name__ == "__main__":

    # Example scores
    message_score = 80
    url_score = 70

    final_score, risk_level = calculate_final_risk(
        message_score,
        url_score,
        has_url=True
    )

    print("--------------------------------")
    print("       RISK ENGINE")
    print("--------------------------------")

    print("Message Score:", message_score)
    print("URL Score:", url_score)

    print("Final Risk Score:", final_score, "/100")
    print("Risk Level:", risk_level)



def generate_explanation(
    detected_keywords,
    url_indicators
):
    """
    Generate human-readable explanations
    from detected indicators.
    """

    explanations = []


    # -----------------------------------
    # Message explanations
    # -----------------------------------

    if "urgent" in detected_keywords:
        explanations.append(
            "🚨 Urgency manipulation detected."
        )

    if "immediately" in detected_keywords:
        explanations.append(
            "⏱️ The message pressures the user to act immediately."
        )

    if "kyc" in detected_keywords:
        explanations.append(
            "🔐 KYC verification request detected."
        )

    if "otp" in detected_keywords:
        explanations.append(
            "🔑 OTP-related content detected."
        )

    if "password" in detected_keywords:
        explanations.append(
            "🔑 Password-related content detected."
        )

    if "bank" in detected_keywords:
        explanations.append(
            "🏦 Financial/bank-related content detected."
        )

    if "blocked" in detected_keywords:
        explanations.append(
            "⚠️ Account-blocking threat detected."
        )

    if "payment" in detected_keywords:
        explanations.append(
            "💳 Payment request detected."
        )

    if "reward" in detected_keywords or "prize" in detected_keywords:
        explanations.append(
            "🎁 Reward/prize-related content detected."
        )


    # -----------------------------------
    # URL explanations
    # -----------------------------------

    for indicator in url_indicators:

        if "HTTPS" in indicator:

            explanations.append(
                "🔗 The URL does not use HTTPS."
            )

        elif "IP address" in indicator:

            explanations.append(
                "🌐 The URL uses an IP address instead of a domain name."
            )

        elif "Suspicious keyword" in indicator:

            explanations.append(
                f"🔎 {indicator}"
            )

        elif "Suspicious-looking domain" in indicator:

            explanations.append(
                f"🌐 {indicator}"
            )

        elif "@ symbol" in indicator:

            explanations.append(
                "⚠️ The URL contains an @ symbol."
            )

        elif "Very long URL" in indicator:

            explanations.append(
                "📏 The URL is unusually long."
            )


    # Remove duplicate explanations
    explanations = list(dict.fromkeys(explanations))


    return explanations