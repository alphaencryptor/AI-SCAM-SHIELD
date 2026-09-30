from urllib.parse import urlparse
import re


# Suspicious words commonly seen in scam URLs
SUSPICIOUS_WORDS = [
    "verify",
    "verification",
    "login",
    "secure",
    "account",
    "kyc",
    "update",
    "password",
    "payment",
    "refund",
    "bank",
    "reward",
    "claim",
    "wallet"
]


# Suspicious-looking TLDs
SUSPICIOUS_TLDS = [
    ".xyz",
    ".top",
    ".click",
    ".shop",
    ".live"
]


def analyze_url(url):

    score = 0
    indicators = []

    # Add https if user forgot the protocol
    if not url.startswith(("http://", "https://")):
        url = "http://" + url

    try:
        parsed = urlparse(url)

        domain = parsed.netloc.lower()
        path = parsed.path.lower()

        # Remove username/password and port if present
        hostname = parsed.hostname

        if hostname is None:
            return 0, ["Invalid URL"]

        # --------------------------------
        # 1. HTTPS check
        # --------------------------------

        if parsed.scheme == "https":
            indicators.append("HTTPS is used")
        else:
            score += 15
            indicators.append("URL does not use HTTPS")

        # --------------------------------
        # 2. IP address instead of domain
        # --------------------------------

        ip_pattern = r"^\d{1,3}(\.\d{1,3}){3}$"

        if re.match(ip_pattern, hostname):
            score += 25
            indicators.append("URL uses an IP address instead of a domain")

        # --------------------------------
        # 3. Very long URL
        # --------------------------------

        if len(url) > 100:
            score += 10
            indicators.append("Very long URL")

        # --------------------------------
        # 4. Suspicious keywords
        # --------------------------------

        for word in SUSPICIOUS_WORDS:

            if word in url.lower():

                score += 5
                indicators.append(
                    f"Suspicious keyword: {word}"
                )

        # --------------------------------
        # 5. Suspicious TLD
        # --------------------------------

        for tld in SUSPICIOUS_TLDS:

            if hostname.endswith(tld):

                score += 15
                indicators.append(
                    f"Suspicious-looking domain ending: {tld}"
                )

        # --------------------------------
        # 6. Too many subdomains
        # --------------------------------

        subdomain_count = hostname.count(".")

        if subdomain_count >= 3:

            score += 10
            indicators.append(
                "Unusually many subdomains"
            )

        # --------------------------------
        # 7. @ symbol
        # --------------------------------

        if "@" in url:

            score += 20
            indicators.append(
                "URL contains @ symbol"
            )

        # --------------------------------
        # 8. Hyphenated domain
        # --------------------------------

        if "-" in hostname:

            score += 5
            indicators.append(
                "Domain contains hyphen"
            )

        # Maximum score
        if score > 100:
            score = 100

        return score, indicators

    except Exception:

        return 0, ["Unable to analyze URL"]



if __name__ == "__main__":

    test_url = "http://sbi-kyc-verification.xyz/login"

    score, indicators = analyze_url(test_url)

    print("--------------------------------")
    print("       URL ANALYZER")
    print("--------------------------------")

    print("URL:", test_url)

    print("Risk Score:", score, "/100")

    print("Detected Indicators:")

    for indicator in indicators:
        print("-", indicator)