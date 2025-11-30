import streamlit as st
from Utilities.html_element_creator import HTMLElementCreator
from Mappers.ml_mapper import SML_CLS_MAPPER, SML_REG_MAPPER, USML_ANADET_MAPPER, USML_CLUS_MAPPER, USML_DIMRED_MAPPER

from Instructions.Machine_Learning.Supervised.Classification.cls_evaluation_metrices import classification_evaluation_metrics
from Instructions.Machine_Learning.Supervised.Regression.reg_evaluation_metrices import regression_evaluation_metrices
from Instructions.Machine_Learning.Unsupervised.Clustering.clus_evaluation_metrices import clustering_evaluation_metrices


st.set_page_config(layout="wide")

html_creator = HTMLElementCreator()
css_file_path = "Style/main.css"
with open(css_file_path) as css:
    st.markdown(f"<style>{css.read()}</style", unsafe_allow_html=True)

st.header("Classical Machine Learning")
st.divider()

try:
    # 1
    st.header("Supervised Learning")
    with st.columns([0.05, 0.95])[1]:
        st.markdown("In supervised learning, the model is trained on a labeled dataset, which means that the input data is paired with the correct output. The goal is to learn a mapping from inputs to outputs.")
        if st.toggle("Classification", key=11):
            st.header("Classification")
            st.markdown(
                'Classification involves predicting categorical labels for new instances based on learned patterns from a labeled dataset.')
            if st.toggle("Evaluation Metrices for Classification"):
                st.markdown(classification_evaluation_metrics)
            for index, (title, value) in enumerate(SML_CLS_MAPPER.items()):

                with st.expander(label=title, expanded=False):
                    st.header(title)
                    html_creator.create_youtube_link_button(
                        label=title, url=value[2])
                    with st.columns([0.6, 0.4])[0]:
                        st.image(image=value[1])
                    st.markdown(value[0])

        if st.toggle("Regression", key=12):
            st.header("Regression")
            st.markdown("Regression predicts continuous numerical values based on input features. The model learns the relationship between the input variables and a continuous output variable")
            if st.toggle("Evaluation Metrices for Regression"):
                st.markdown(regression_evaluation_metrices)
            for index, (title, value) in enumerate(SML_REG_MAPPER.items()):
                with st.expander(label=title, expanded=False):
                    st.header(title)
                    html_creator.create_youtube_link_button(
                        label=title, url=value[2])
                    with st.columns([0.6, 0.4])[0]:
                        st.image(image=value[1])
                    st.markdown(value[0])

    # 2
    st.header("Unsupervised Learning")
    with st.columns([0.05, 0.95])[1]:
        st.markdown("Unsupervised Learning is a type of machine learning where the algorithm learns from unlabeled data. Unlike supervised learning,which requires labeled data to train the model, unsupervised learning finds patterns, structures, or relationships within the data itself.")
        if st.toggle("Clustering", key=21):
            st.header("Clustering")
            st.markdown(
                'Clustering is an unsupervised learning technique that groups similar data points together based on their features. The goal is to identify distinct groups (clusters) in the data without prior labels.')
            if st.toggle("Evaluation Metrices for Clustering"):
                st.markdown(clustering_evaluation_metrices)
            for index, (title, value) in enumerate(USML_CLUS_MAPPER.items()):
                with st.expander(label=title, expanded=False):
                    st.header(title)
                    html_creator.create_youtube_link_button(
                        label=title, url=value[2])
                    with st.columns([0.6, 0.4])[0]:
                        st.image(image=value[1])
                    st.markdown(value[0])

        if st.toggle("Dimensionality Reduction", key=22):
            st.header("Dimensionality Reduction")
            st.markdown("Dimensionality reduction reduces the number of features (dimensions) in a dataset while retaining essential information. This is useful for simplifying data, visualizing high-dimensional data, and improving computational efficiency. ")
            for index, (title, value) in enumerate(USML_DIMRED_MAPPER.items()):
                with st.expander(label=title, expanded=False):
                    st.header(title)
                    html_creator.create_youtube_link_button(
                        label=title, url=value[2])
                    with st.columns([0.6, 0.4])[0]:
                        st.image(image=value[1])
                    st.markdown(value[0])

        if st.toggle("Anomaly Detection", key=23):
            st.header("Anomaly Detection")
            st.markdown("Anomaly detection identifies rare or unusual observations in a dataset that deviate significantly from the norm. This technique is valuable for spotting outliers that may indicate fraud, errors, or other significant events. ")
            for index, (title, value) in enumerate(USML_ANADET_MAPPER.items()):
                with st.expander(label=title, expanded=False):
                    st.header(title)
                    html_creator.create_youtube_link_button(
                        label=title, url=value[2])
                    with st.columns([0.6, 0.4])[0]:
                        st.image(image=value[1])
                    st.markdown(value[0])

    # 3
    st.header("Reinforcement Learning")
    with st.columns([0.05, 0.95])[1]:
        st.markdown("Reinforcement Learning is a type of machine learning where an agent learns to make decisions by interacting with an environment. The agent receives rewards or penalties based on its actions, and its goal is to maximize its cumulative reward over time.")


except Exception as e:
    st.markdown("# Check Instruction File")
    st.error(e)
