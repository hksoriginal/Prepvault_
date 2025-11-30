import streamlit as st
from Utilities.html_element_creator import HTMLElementCreator
from Mappers.dsa_mapper import DSA_MAPPER

st.set_page_config(layout="wide")

html_creator = HTMLElementCreator()
css_file_path = "Style/main.css"
with open(css_file_path) as css:
    st.markdown(f"<style>{css.read()}</style", unsafe_allow_html=True)



try:
    st.markdown("## DSA for AI/ML Roles")
    for index, (title, value) in enumerate(DSA_MAPPER.items()):
        with st.expander(label=title, expanded=False):
            html_creator.create_leetcode_link_button(label=title, url=value[1])

            html_creator.create_youtube_link_button(label=title, url=value[2])
            st.markdown(value[0])

except Exception:
    st.markdown("# Check Instruction File")
