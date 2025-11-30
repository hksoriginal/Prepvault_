import streamlit as st
import plotly.express as px
import pandas as pd

data = dict(
    ids=["AI", "ML", "DL", "Supervised", "Unsupervised"],
    labels=["AI", "ML", "DL", "Supervised", "Unsupervised"],
    parents=["", "AI", "ML", "DL", "DL"]
)

fig = px.sunburst(data, names='labels', parents='parents')
st.plotly_chart(fig)
