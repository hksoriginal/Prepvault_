import streamlit as st
from Mappers.guide_mapper import GUIDE_MAPPER

st.set_page_config(page_title="Quick Guide", page_icon="📘", layout="wide")

# --- Modern CSS for Streamlit ---
st.markdown("""
<style>
/* Page background */
body {
    background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
    color: #f0f0f0;
}

/* Expander styling */
div[role="button"] {
    background-color: #1e293b !important;
    border-radius: 12px;
    padding: 12px;
    margin-bottom: 8px;
    border: 1px solid #334155;
    font-weight: bold;
    transition: 0.3s;
}

div[role="button"]:hover {
    background-color: #334155 !important;
    cursor: pointer;
}

/* Expander content */
div[data-testid="stExpander"] > div {
    background-color: #1e293b;
    border-radius: 0 0 12px 12px;
    padding: 12px;
    color: #f8fafc;
    font-size: 15px;
}

/* Headers */
h2 {
    color: #f8fafc;
    text-align: center;
    font-family: 'Segoe UI', sans-serif;
    margin-bottom: 24px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("## Quick Guide")

try:
    for title, value in GUIDE_MAPPER.items():
        with st.expander(label=title, expanded=False):
            st.markdown(value)
except Exception:
    st.error("⚠️ Check Instruction File")
