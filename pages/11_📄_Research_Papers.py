import streamlit as st
import requests
import xml.etree.ElementTree as ET

st.set_page_config(page_title="ArXiv Paper Explorer",
                   page_icon="🤖", layout="wide")

# --- Optional gradient background ---
st.markdown("""
<style>
body {
    background: radial-gradient(circle at 20% 20%, #0a0a0f, #050507);
}
</style>
""", unsafe_allow_html=True)

st.title("🤖 ArXiv Research Paper Explorer")
search_cols = st.columns([1, 3])
# --- Topic Selection as Tags ---
with search_cols[1]:
    topics = st.multiselect(
        "🎯 Select Topics:",
        [
            "artificial intelligence", "machine learning", "deep learning",
            "natural language processing", "computer vision",
            "reinforcement learning", "Generative AI", "Agentic AI", "AI Agents", "Neural Networks",
            "Transformers", "GPT", "BERT", "Convolutional Neural Networks",
            "Recurrent Neural Networks", "AI Ethics", "AI Safety", "AI Interpretability",
            "AI Fairness", "AI Robustness", "AI Optimization", "AI in Healthcare",
            "AI in Finance", "AI in Robotics", "AI in Education", "AI in Gaming",
            "AI in Autonomous Vehicles", "AI in Natural Sciences", "AI in Social Sciences", ""
        ],
        default=["artificial intelligence", "machine learning"],
        accept_new_options=True
    )

# --- Dropdown for number of results ---
with search_cols[0]:
    num_results = st.selectbox("📄 Number of Results", [
        5, 10, 20, 30, 40, 50], index=1)

# --- Always keep sort order descending (latest first) ---
sort_param = "descending"

# --- Build combined topic query for arXiv API ---
if topics:
    combined_query = "+OR+".join(
        [f"all:{t.replace(' ', '+')}" for t in topics])
else:
    combined_query = "all:artificial+intelligence"

url = (
    f"http://export.arxiv.org/api/query?"
    f"search_query={combined_query}"
    f"&start=0&max_results={num_results}"
    f"&sortBy=submittedDate&sortOrder={sort_param}"
)

# --- Automatically fetch data ---
with st.spinner("Fetching latest research papers..."):
    response = requests.get(url)

if response.status_code != 200:
    st.error("❌ Failed to fetch data from arXiv API.")
else:
    root = ET.fromstring(response.text)
    entries = root.findall("{http://www.w3.org/2005/Atom}entry")

    if not entries:
        st.warning("No results found.")
    else:

        # --- Display in 2-column glass cards ---
        for i in range(0, len(entries), 2):
            cols = st.columns(2)
            for j in range(2):
                if i + j < len(entries):
                    entry = entries[i + j]
                    title = entry.find(
                        "{http://www.w3.org/2005/Atom}title").text.strip()
                    summary = entry.find(
                        "{http://www.w3.org/2005/Atom}summary").text.strip()
                    authors = [
                        a.find("{http://www.w3.org/2005/Atom}name").text
                        for a in entry.findall("{http://www.w3.org/2005/Atom}author")
                    ]
                    link = entry.find("{http://www.w3.org/2005/Atom}id").text
                    published = entry.find(
                        "{http://www.w3.org/2005/Atom}published").text[:10]
                    pdf_link = link.replace("/abs/", "/pdf/") + ".pdf"

                    # --- Glass-style Card with PDF button ---
                    with cols[j]:
                        st.markdown(
                            f"""
                            <div style="
                                background: rgba(255, 255, 255, 0.08);
                                backdrop-filter: blur(12px);
                                -webkit-backdrop-filter: blur(12px);
                                border: 1px solid rgba(255, 255, 255, 0.15);
                                border-radius: 18px;
                                padding: 20px;
                                margin-bottom: 25px;
                                box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2);
                                transition: transform 0.2s ease, box-shadow 0.2s ease;
                            " 
                            onmouseover="this.style.transform='scale(1.02)'; this.style.boxShadow='0 10px 25px rgba(0,0,0,0.35)';" 
                            onmouseout="this.style.transform='scale(1)'; this.style.boxShadow='0 8px 24px rgba(0,0,0,0.2)';"
                            >
                                <h3 style="color:#00c6ff; margin-bottom:8px;">
                                    <a href="{link}" target="_blank" style="text-decoration:none; color:#00c6ff;">{title}</a>
                                </h3>
                                <p style="color:#ccc; font-size:14px; margin:5px 0;">
                                    <b>📅 Published:</b> {published}
                                </p>
                                <p style="color:#ccc; font-size:14px; margin:5px 0;">
                                    <b>👥 Authors:</b> {', '.join(authors)}{" ..." if len(authors) > 20 else ""}
                                </p>
                                <p style="color:#aaa; font-size:14px; line-height:1.4; margin-top:10px;">
                                    📝 {summary[:350]}...
                                </p>
                                <div style="text-align:right; margin-top:15px;">
                                    <a href="{pdf_link}" target="_blank" style="
                                        display:inline-block;
                                        background:linear-gradient(135deg,#00c6ff,#0072ff);
                                        color:white;
                                        padding:8px 16px;
                                        border-radius:12px;
                                        text-decoration:none;
                                        font-size:14px;
                                        font-weight:600;
                                        transition: background 0.2s ease;
                                    " 
                                    onmouseover="this.style.background='linear-gradient(135deg,#0099ff,#005ce6)';"
                                    onmouseout="this.style.background='linear-gradient(135deg,#00c6ff,#0072ff)';">
                                        📄 View PDF
                                    </a>
                                </div>
                            </div>
                            """,
                            unsafe_allow_html=True
                        )
