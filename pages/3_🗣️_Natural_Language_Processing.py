import streamlit as st
from Instructions.NLP.nlp_interview_q import NLP_INTERVIEW_Q
from Mappers.nlp_mapper import NLP_CONCEPTS_MAPPER, BERT_MAPPER
from Utilities.html_element_creator import HTMLElementCreator


st.set_page_config(layout="wide")

html_creator = HTMLElementCreator()
css_file_path = "Style/main.css"
with open(css_file_path) as css:
    st.markdown(f"<style>{css.read()}</style", unsafe_allow_html=True)

st.header("Natural Language Processing ")
st.markdown("Natural Language Processing (NLP) is a field of artificial intelligence focused on enabling computers to understand, interpret, and generate human language. By combining techniques from linguistics, computer science, and machine learning, NLP allows machines to process text and speech in meaningful ways. Common NLP tasks include text classification, sentiment analysis, machine translation, and question answering. Modern advancements, particularly in deep learning and models like BERT and GPT, have significantly improved the ability of machines to handle complex language tasks, making NLP crucial for applications such as chatbots, language translation, and personal assistants.")
st.divider()

try:
    st.header("NLP Concepts")
    with st.columns([0.05, 0.95])[1]:
        st.markdown("Common NLP Concepts")
        for index, (title, value) in enumerate(NLP_CONCEPTS_MAPPER.items()):
            with st.expander(label=title, expanded=False):
                st.header(title)
                html_creator.create_youtube_link_button(
                    label=title, url=value[2])
                with st.columns([0.7, 0.3])[0]:
                    if len(value[1]) >= 1:
                        for image_path in value[1]:
                            st.image(image=image_path,
                                     caption=(image_path.split('/')[-1].split(".")[0]).capitalize())
                st.markdown(value[0])

    # 1
    st.header("Bidirectional Encoder Representations from Transformers (BERT)")
    with st.columns([0.05, 0.95])[1]:
        st.markdown("BERT (Bidirectional Encoder Representations from Transformers) is a powerful language model that has revolutionized the field of natural language processing (NLP). It's composed of several key components that work together to process and understand text.")
        for index, (title, value) in enumerate(BERT_MAPPER.items()):
            with st.expander(label=title, expanded=False):
                st.header(title)
                html_creator.create_youtube_link_button(
                    label=title, url=value[2])
                with st.columns([0.6, 0.4])[0]:
                    st.image(image=value[1])
                st.markdown(value[0], unsafe_allow_html=True)
    
    st.divider()
    with st.expander("Interview Questions"):
        st.image('./Instructions/NLP/nlp_int.png')
        st.markdown(NLP_INTERVIEW_Q)


except Exception as e:
    st.markdown("# Check Instruction File")
    st.error(e)
