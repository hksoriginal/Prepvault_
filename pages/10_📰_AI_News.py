import streamlit as st
import requests
import webbrowser

API_KEY = "8d1b3b0630184466aa95073a4ebf0c55"

st.set_page_config(page_title="AI & GenAI Advancements", layout="wide")

st.title("🤖 AI & Generative AI - Latest Technological Advancements")
st.write("Real-time updates on breakthroughs in AI research, LLMs, neural networks, and deep learning.")

url = "https://newsapi.org/v2/everything"

params = {
    "q": (
        "(artificial intelligence AND advancement) OR "
        "(machine learning AND (research OR breakthrough OR model OR architecture)) OR "
        "(deep learning AND (research OR neural network OR paper)) OR "
        "\"large language model\" OR LLM OR \"transformer model\" OR "
        "(AI AND (research OR model OR benchmark OR algorithm))"
    ),
    "language": "en",
    "sortBy": "publishedAt",
    "apiKey": API_KEY
}

try:
    response = requests.get(url, params=params)
    data = response.json()
except Exception as e:
    st.error(f"❌ Failed to fetch news: {e}")
    st.stop()

articles = data.get("articles", [])

if not articles:
    st.warning("⚠️ No technical AI advancement news found. Try again later.")
else:
    for i in range(0, len(articles), 2):
        col1, col2 = st.columns(2)

        # ---------------- CARD 1 ----------------
        if i < len(articles):
            a = articles[i]
            with col1:
                with st.container(border=True):
                    st.markdown(f"### 🔍 {a['title']}")
                    if a.get("urlToImage"):
                        st.image(a["urlToImage"], use_container_width=True)
                    st.write(a.get("description", "No description available."))

                    # Button for full article
                    if st.button("📖 View Full Article", key=f"a_{i}"):
                        webbrowser.open_new_tab(a["url"])

        # ---------------- CARD 2 ----------------
        if i + 1 < len(articles):
            b = articles[i + 1]
            with col2:
                with st.container(border=True):
                    st.markdown(f"### 🔍 {b['title']}")
                    if b.get("urlToImage"):
                        st.image(b["urlToImage"], use_container_width=True)
                    st.write(b.get("description", "No description available."))

                    # Button for full article
                    if st.button("📖 View Full Article", key=f"b_{i}"):
                        webbrowser.open_new_tab(b["url"])
