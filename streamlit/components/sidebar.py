import streamlit as st

def render_sidebar():

    with st.sidebar:

        st.page_link(
            "pages/home.py",
            label="Home",
            icon="🏠"
        )

        st.page_link(
            "pages/prediction.py",
            label="Prediction",
            icon="🔮"
        )

        # st.page_link(
        #     "pages/analytics.py",
        #     label="Analytics",
        #     icon="📊"
        # )

        # st.page_link(
        #     "pages/history.py",
        #     label="History",
        #     icon="📜"
        # )