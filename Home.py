
from Mappers.documentation_mapper import DOCUMENTATION_MAPPER
from Utilities.html_element_creator import HTMLElementCreator
import streamlit as st
import streamlit.components.v1 as components




st.set_page_config(
    page_title="Prepvault",
    layout="wide",
)

css_file_path = "Style/main.css"
with open(css_file_path) as css:
    st.markdown(f"<style>{css.read()}</style", unsafe_allow_html=True)

st.markdown("# PrepVault -  Comprehensive Preparation Vault")


placeholder = st.empty()


authentication_status = True
name = "Admin"

if authentication_status:

    element_creator = HTMLElementCreator()

    try:
        documentation_columns = st.columns(len(DOCUMENTATION_MAPPER))
        st.markdown("## Documentations")
        for index, (title, value) in enumerate(DOCUMENTATION_MAPPER.items()):
            element_creator.create_link_button(title, value)

    except Exception:
        st.markdown("# Check Instruction File")

elif authentication_status == False:
    st.error("Username/password is incorrect")
elif authentication_status == None:
    st.warning("Please enter your username and password")
