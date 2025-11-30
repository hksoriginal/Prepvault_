import streamlit as st

from Mappers.guide_mapper import GUIDE_MAPPER


st.set_page_config(layout="wide")

css_file_path = "Style/main.css"
with open(css_file_path) as css:
    st.markdown(f"<style>{css.read()}</style", unsafe_allow_html=True)


try:
    st.markdown("## Quick Guide")
    for index, (title, value) in enumerate(GUIDE_MAPPER.items()):
        with st.expander(label=title, expanded=False):
            st.markdown(value)

except Exception:
    st.markdown("# Check Instruction File")
