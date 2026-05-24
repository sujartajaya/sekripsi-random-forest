import streamlit as st
from services.api import get_questions, predict
from utils.style import load_css
from components.sidebar import render_sidebar

# =========================================
# CONFIG
# =========================================

st.set_page_config(
    page_title="Prediction",
    page_icon="🔮",
    layout="wide"
)

render_sidebar()

# =========================================
# CSS
# =========================================

load_css()

st.markdown("""
<style>

.block-container {
    padding-top: 2rem;
}

.title {
    font-size: 38px;
    font-weight: bold;
    color: #00FFAA;
}

</style>
""", unsafe_allow_html=True)

# =========================================
# HEADER
# =========================================

st.markdown(
    """
    <div class="title">
        🔮 Autism Prediction
    </div>
    """,
    unsafe_allow_html=True
)

st.write("Please answer the following questions.")

st.divider()

# =========================================
# LOAD QUESTIONS
# =========================================

try:

    data = get_questions()

    questions = data.get("questions", [])

except Exception as e:

    st.error(f"Failed load questions: {e}")
    st.stop()

# =========================================
# FORM
# =========================================

answers = {}

with st.form("prediction_form"):

    for q in questions:

        field = q["field"]
        question = q["question"]
        qtype = q["type"]

        # =========================================
        # BINARY
        # =========================================

        if qtype == "binary":

            value = st.radio(
                question,
                ["Yes", "No"],
                horizontal=True
            )

            answers[field] = 1 if value == "Yes" else 0

        # =========================================
        # INTEGER
        # =========================================

        elif qtype == "integer":

            value = st.number_input(
                question,
                min_value=0,
                step=1
            )

            answers[field] = value

        # =========================================
        # CATEGORICAL
        # =========================================

        elif qtype == "categorical":

            choices = q.get("choices", [])

            value = st.selectbox(
                question,
                choices
            )

            answers[field] = value

    # =========================================
    # SUBMIT BUTTON
    # =========================================

    submitted = st.form_submit_button(
        "🚀 Predict",
        use_container_width=True
    )

# =========================================
# PREDICTION
# =========================================

if submitted:

    with st.spinner("Processing prediction..."):

        try:

            payload = answers

            result = predict(payload)

            prediction_data = result.get("prediction", {})

            prediction = prediction_data.get("prediction", 0)

            label = prediction_data.get(
                "label",
                "Unknown"
            )

            probability_data = prediction_data.get(
                "probability",
                {}
            )

            probability = probability_data.get("asd", 0)


            st.divider()

            st.subheader("📊 Prediction Result")

            # =========================================
            # RESULT
            # =========================================

            if prediction == 1:

                st.error("⚠️ High Risk Detected")

            else:

                st.success("✅ Low Risk Detected")

            # =========================================
            # PROBABILITY
            # =========================================

            st.subheader("Confidence")

            st.progress(probability / 100)

            st.metric(
                "Probability",
                f"{probability}%"
            )

            # =========================================
            # RAW JSON
            # =========================================

            with st.expander("📦 API Response"):

                st.json(result)

        except Exception as e:

            st.error(f"Prediction error: {e}")