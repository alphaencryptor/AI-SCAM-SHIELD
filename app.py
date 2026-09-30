import streamlit as st
from PIL import Image

from scam_detector import analyze_message
from url_analyzer import analyze_url
from risk_engine import calculate_final_risk
from ocr_engine import extract_text_from_image
from explanation_engine import generate_explanation
from ml_detector import predict_scam
from multilingual_engine import detect_language


# --------------------------------
# PAGE CONFIG
# --------------------------------

st.set_page_config(
    page_title="AI ScamShield",
    page_icon="🛡️",
    layout="centered"
)

st.markdown("""
<style>

    /* Main background */
    .stApp {
        background-color: #0b0f19;
    }

    /* Main container */
    .block-container {
        max-width: 900px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    /* Header */
    .main-title {
        text-align: center;
        font-size: 3rem;
        font-weight: 800;
        margin-bottom: 0.2rem;
    }

    .subtitle {
        text-align: center;
        color: #9ca3af;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }

    /* Cards */
    .card {
        background: #151a27;
        border: 1px solid #252c3d;
        border-radius: 16px;
        padding: 20px;
        margin-bottom: 20px;
    }

    /* Risk card */
    .risk-card {
        background: #151a27;
        border: 1px solid #3a4255;
        border-radius: 18px;
        padding: 30px;
        text-align: center;
        margin-top: 25px;
        margin-bottom: 25px;
    }

    .risk-score {
        font-size: 4rem;
        font-weight: 800;
    }

    .risk-label {
        font-size: 1.4rem;
        font-weight: 700;
    }

    /* Indicator */
    .indicator {
        background: #151a27;
        border: 1px solid #252c3d;
        border-radius: 10px;
        padding: 10px 14px;
        margin: 6px 0;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #6b7280;
        margin-top: 40px;
        font-size: 0.9rem;
    }

</style>
""", unsafe_allow_html=True)

# --------------------------------
# HEADER
# --------------------------------

st.markdown(
    """
    <div class="card">
        <b>Protect yourself from digital scams.</b><br><br>
        Analyze suspicious messages, URLs and screenshots
        using OCR, multilingual detection, machine learning
        and risk analysis.
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'AI-Powered Scam Detection & Protection'
    '</div>',
    unsafe_allow_html=True
)



st.write(
    "Analyze suspicious messages, URLs, and screenshots "
    "using rule-based detection, machine learning and OCR."
)


# --------------------------------
# MESSAGE INPUT
# --------------------------------
st.markdown("### 📩 Analyze a Suspicious Message")
message = st.text_area(
    "📩 Suspicious Message",
    height=180,
    placeholder=(
        "Paste a suspicious SMS, WhatsApp message or email here..."
    )
)


# --------------------------------
# URL INPUT
# --------------------------------
st.markdown("### 🔗 Analyze a Suspicious URL")

url = st.text_input(
    "Suspicious URL",
    placeholder="https://example.com",
    label_visibility="collapsed"
)


# --------------------------------
# SCREENSHOT INPUT
# --------------------------------

st.markdown("### 📸 Upload Screenshot")

uploaded_image = st.file_uploader(
    "📸 Upload Suspicious Screenshot",
    type=["png", "jpg", "jpeg"]
)


# --------------------------------
# ANALYZE BUTTON
# --------------------------------

if st.button("🔍 ANALYZE MESSAGE"):


    # --------------------------------
    # OCR
    # --------------------------------



    ocr_text = ""

    if uploaded_image is not None:

        st.divider()

        st.subheader("📸 Screenshot Analysis")

        image = Image.open(uploaded_image)

        st.image(
            image,
            caption="Uploaded Screenshot",
            use_container_width=True
        )

        # OCR extraction
        ocr_text = extract_text_from_image(image)

        st.subheader("📝 Extracted Text")

        st.text_area(
            "OCR Result",
            ocr_text,
            height=180
        )


    # --------------------------------
    # SELECT TEXT
    # --------------------------------

    analysis_text = message

    if not analysis_text.strip() and ocr_text.strip():

        analysis_text = ocr_text


    # --------------------------------
    # INPUT VALIDATION
    # --------------------------------

    if (
        not analysis_text.strip()
        and not url.strip()
    ):

        st.warning(
            "⚠️ Please enter a message, upload a screenshot, "
            "or enter a URL."
        )

    else:

        # --------------------------------
        # MESSAGE DETECTOR
        # --------------------------------

        score = 0
        risk_level = "LOW"
        detected_keywords = []

        if analysis_text.strip():

            score, risk_level, detected_keywords = analyze_message(
                analysis_text
            )


        # --------------------------------
        # LANGUAGE DETECTION
        # --------------------------------

        detected_language = "Unknown"

        if analysis_text.strip():

            detected_language = detect_language(
                analysis_text
            )


        # --------------------------------
        # MACHINE LEARNING
        # --------------------------------

        ml_prediction = None
        ml_probability = 0

        if analysis_text.strip():

            ml_prediction, ml_probability = predict_scam(
                analysis_text
            )


        # --------------------------------
        # URL ANALYSIS
        # --------------------------------

        url_score = 0
        url_indicators = []

        if url.strip():

            url_score, url_indicators = analyze_url(
                url
            )


        # --------------------------------
        # FINAL RISK ENGINE
        # --------------------------------

        final_score, final_risk_level = calculate_final_risk(
            score,
            url_score,
            has_url=bool(url.strip())
        )


        # --------------------------------
        # EXPLANATION ENGINE
        # --------------------------------

        explanations = generate_explanation(
            detected_keywords,
            url_indicators,
            ml_prediction,
            ml_probability
        )


        # =================================
        # DISPLAY RESULTS
        # =================================

        st.divider()

        st.header("🚨 Scam Analysis Result")


        # --------------------------------
        # RISK SCORE
        # --------------------------------

        st.markdown(
    f"""
    <div class="risk-card">

        <div style="color:#9ca3af;">
            OVERALL RISK SCORE
        </div>

        <div class="risk-score">
            {final_score}/100
        </div>

        <div class="risk-label">
            🚨 {final_risk_level}
        </div>

    </div>
    """,
    unsafe_allow_html=True
)

        # --------------------------------
        # LANGUAGE
        # --------------------------------

        if analysis_text.strip():

            st.subheader("🌐 Language Detection")

            st.write(
                f"Detected Language: **{detected_language}**"
            )


        # --------------------------------
        # ML RESULT
        # --------------------------------

        if analysis_text.strip():

            st.subheader("🤖 AI Model Analysis")

            st.write(
                f"Prediction: **{ml_prediction}**"
            )

            st.write(
                f"Scam Probability: **{ml_probability}%**"
            )


        # --------------------------------
        # DETECTED KEYWORDS
        # --------------------------------

        if detected_keywords:

         st.subheader("🔎 Detected Indicators")

        for keyword in detected_keywords:

         st.markdown(
            f"""
            <div class="indicator">
                🔍 {keyword}
            </div>
            """,
            unsafe_allow_html=True
        )


        # --------------------------------
        # URL INDICATORS
        # --------------------------------

        if url_indicators:

            st.subheader("🔗 URL Indicators")

            for indicator in url_indicators:

                st.write(
                    f"• {indicator}"
                )


        # --------------------------------
        # WHY SUSPICIOUS
        # --------------------------------

        st.subheader(
            "🧠 Why is this suspicious?"
        )

        for explanation in explanations:

            st.write(
                explanation
            )


        # --------------------------------
        # RECOMMENDATION
        # --------------------------------

        st.subheader(
            "🛡️ Recommended Action"
        )

        if final_score >= 75:

            st.error(
                "🚨 HIGH RISK: Do not click suspicious links "
                "or share OTPs, passwords, banking information "
                "or payment details. Verify the request using "
                "an official source."
            )

        elif final_score >= 50:

            st.warning(
                "⚠️ SUSPICIOUS: Verify the sender and website "
                "through an official source before taking action."
            )

        else:

            st.success(
                "✅ LOW RISK based on the current prototype "
                "analysis. Continue to use normal security precautions."
            )


st.markdown(
    """
    <div class="footer">
        🛡️ AI ScamShield · Hackathon Prototype<br>
        Stay alert. Verify before you trust.
    </div>
    """,
    unsafe_allow_html=True
)