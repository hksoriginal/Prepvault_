import streamlit as st
from Mappers.github_mapper import repositories
from Utilities.html_element_creator import HTMLElementCreator

html_element_creator = HTMLElementCreator()

st.set_page_config(
    page_title="Important Github Repositories",
    page_icon="😼",
    layout="wide",
)


css_file_path = "Style/main.css"
# with open(css_file_path) as css:
#     st.markdown(f"<style>{css.read()}</style", unsafe_allow_html=True)