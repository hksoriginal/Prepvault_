import streamlit as st
from Mappers.gen_ai_mapper import GENAI_MAPPER
from Utilities.html_element_creator import HTMLElementCreator

st.set_page_config(
    page_title="Generative AI",
    page_icon="💬",
    layout="wide",
)

html_creator = HTMLElementCreator()
css_file_path = "Style/main.css"
with open(css_file_path) as css:
    st.markdown(f"<style>{css.read()}</style", unsafe_allow_html=True)


try:
    st.markdown("## Generative AI")
    for index, (title, value) in enumerate(GENAI_MAPPER.items()):
        with st.expander(label=title, expanded=False):
            st.image(value[1])
            st.markdown(value[0])


except Exception:
    st.markdown("# Check Instruction File")
