import streamlit as st

# def load_css():

#     st.markdown("""
#     <style>

#     /* Hide Streamlit toolbar */
#     [data-testid="stToolbar"] {
#         display: none;
#     }

#     /* Hide hamburger menu */
#     #MainMenu {
#         visibility: hidden;
#     }

#     /* Hide footer */
#     footer {
#         visibility: hidden;
#     }

#     /* Hide header */
#     header {
#         visibility: hidden;
#     }

#     </style>
#     """, unsafe_allow_html=True)

def load_css():

    st.markdown("""
    <style>

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header {
        visibility: hidden;
    }

    [data-testid="stToolbar"] {
        display: none;
    }

    [data-testid="collapsedControl"] {
        display: none;
    }

    [data-testid="stDecoration"] {
        display: none;
    }

    /* Hide app.py menu item */
    [data-testid="stSidebarNav"] ul li:first-child {
        display: none;
    }

    [data-testid="stSidebarNav"] {
        display: none;
    }
    
    </style>
    """, unsafe_allow_html=True)