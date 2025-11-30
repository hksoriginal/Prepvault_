import streamlit as st
from Utilities.html_element_creator import HTMLElementCreator
from Mappers.dsa_mapper import DSA_MAPPER

st.set_page_config(page_title="DSA for AI/ML Roles", page_icon="🧩", layout="wide")

# --- Modern CSS Styling ---
st.markdown("""
<style>
/* Page background */
body {
    background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
    color: #f0f0f0;
    font-family: 'Segoe UI', sans-serif;
}

/* Expander styling */
div[role="button"] {
    background-color: #1e293b !important;
    border-radius: 12px;
    padding: 12px;
    margin-bottom: 12px;
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
    padding: 16px;
    color: #f8fafc;
}

/* Buttons inside expander */
a.button {
    display: inline-block;
    background-color: #2563eb;
    color: white !important;
    padding: 8px 16px;
    margin: 4px 4px 12px 0;
    border-radius: 8px;
    text-decoration: none;
    font-weight: 500;
    transition: 0.3s;
}

a.button:hover {
    background-color: #1e40af;
}
</style>
""", unsafe_allow_html=True)

st.markdown("## DSA for AI/ML Roles")

html_creator = HTMLElementCreator()

try:
    for title, value in DSA_MAPPER.items():
        with st.expander(label=title, expanded=False):
            # LeetCode button
            html_creator.create_leetcode_link_button(label=title, url=value[1])
            # YouTube button
            html_creator.create_youtube_link_button(label=title, url=value[2])
            # Description
            st.markdown(value[0])

except Exception:
    st.error("⚠️ Check Instruction File")
