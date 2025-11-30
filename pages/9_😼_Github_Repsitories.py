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
with open(css_file_path) as css:
    st.markdown(f"<style>{css.read()}</style", unsafe_allow_html=True)


grid_cols = st.columns(3)

for idx, (title, url) in enumerate(repositories.items()):
    col = grid_cols[idx % 3]
    with col:
        st.text("")
        html_element_creator.create_github_card(repo_url=url, title=title)
