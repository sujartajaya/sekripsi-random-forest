import streamlit as st
import pandas as pd
from utils.style import load_css
from components.sidebar import render_sidebar
import requests
from services.api import get_model_info

# =========================================
# CONFIG
# =========================================

st.set_page_config(
    page_title="Home",
    page_icon="🏠",
    layout="wide"
)

render_sidebar()

# =========================================
# CUSTOM CSS
# =========================================
load_css()

st.markdown("""
<style>

.block-container {
    padding-top: 2rem;
}

.main-title {
    font-size: 42px;
    font-weight: bold;
    color: #00FFAA;
}

.sub-title {
    font-size: 18px;
    color: #BBBBBB;
}

.card {
    background-color: #1E1E1E;
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #333333;
}

</style>
""", unsafe_allow_html=True)

# =========================================
# HEADER
# =========================================

st.markdown(
    """
    <div class="main-title">
        🌲 Random Forest Dashboard
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="sub-title">
        Sistem Prediksi Machine Learning menggunakan algoritma Random Forest
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

# =========================================
# METRIC
# =========================================
meta_info = get_model_info()

try:
    accuracy = meta_info["model_info"]["accuracy"]
    precision = meta_info["model_info"]["precision"]
    recall = meta_info["model_info"]["recall"]
    dataset_rows = meta_info["model_info"]["dataset_rows"]

except KeyError:
    accuracy = "N/A"
    precision = "N/A"
    recall = "N/A"
    dataset_rows = "N/A"    

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    label="Accuracy",
    value=f"{accuracy * 100:.2f}%" if isinstance(accuracy, (int, float)) else accuracy
)

col2.metric(
    label="Precision",
    value=f"{precision * 100:.2f}%" if isinstance(precision, (int, float)) else precision
)

col3.metric(
    label="Recall",
    value=f"{recall * 100:.2f}%" if isinstance(recall, (int, float)) else recall
)

col4.metric(
    label="Dataset",
    value=f"{dataset_rows} Rows" if isinstance(dataset_rows, (int, float)) else dataset_rows
)

# =========================================
# MAIN CONTENT
# =========================================

left, right = st.columns([2, 1])

# =========================================
# LEFT CONTENT
# =========================================

with left:

    st.subheader("📌 Tentang Project")

    st.write("""
    Dashboard ini digunakan untuk melakukan prediksi data menggunakan 
    algoritma Random Forest yang dibangun menggunakan Python dan FastAPI.

    Sistem ini mendukung:
    
    - Prediksi realtime
    - Analisis model
    - Visualisasi data
    - History prediksi
    - Monitoring hasil machine learning
    """)

    st.subheader("🧠 Algoritma")

    st.info("""
    Random Forest adalah algoritma ensemble learning yang menggunakan
    banyak decision tree untuk meningkatkan akurasi prediksi dan
    mengurangi overfitting.
    """)

# =========================================
# RIGHT CONTENT
# =========================================

with right:

    st.subheader("⚡ Status System")

    st.success("✅ FastAPI Connected")
    st.success("✅ Model Loaded")
    st.success("✅ Streamlit Running")

    st.subheader("📊 Model Information")

    info = {
        "Model": "Random Forest",
        "Trees": 100,
        "Criterion": "gini",
        "Random State": 42
    }

    st.json(info)

# =========================================
# SAMPLE DATA
# =========================================

st.divider()

st.subheader("📋 Sample Dataset")

sample_data = pd.DataFrame({
    "Feature 1": [12, 15, 20],
    "Feature 2": [30, 18, 25],
    "Feature 3": [1, 0, 1],
    "Target": [0, 1, 1]
})

st.dataframe(
    sample_data,
    use_container_width=True
)

# =========================================
# FOOTER
# =========================================

st.divider()

st.caption("Random Forest Machine Learning Dashboard • FastAPI + Streamlit")