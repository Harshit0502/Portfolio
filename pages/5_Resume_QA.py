import streamlit as st
import json
from pathlib import Path
from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="Resume Q&A — Harshit Mahour", page_icon="❓", layout="wide")
DATA_PATH = Path("data/portfolio.json")

@st.cache_data
def load_data():
    return json.loads(DATA_PATH.read_text(encoding="utf-8"))

@st.cache_data
def read_pdf_text(pdf_path: str) -> str:
    try:
        reader = PdfReader(pdf_path)
        text = "\n".join(page.extract_text() or "" for page in reader.pages)
        return text
    except Exception:
        return ""

@st.cache_data
def chunk_text(text: str, size: int = 600):
    words = text.split()
    chunks = []
    for i in range(0, len(words), size):
        chunks.append(" ".join(words[i:i+size]))
    return chunks

st.title("❓ Ask about my Resume")

data = load_data()
resume_local = data.get("resume_local_path", "")  # optional local fallback
resume_drive = data.get("resume_url", "")

st.caption("Upload your resume PDF here OR place a local path in JSON (resume_local_path). Drive link is shown below as reference.")

uploaded = st.file_uploader("Upload Resume PDF", type=["pdf"])
text = ""
if uploaded:
    try:
        reader = PdfReader(uploaded)
        text = "\n".join(page.extract_text() or "" for page in reader.pages)
    except Exception:
        st.error("Could not parse the uploaded PDF.")
elif resume_local:
    text = read_pdf_text(resume_local)

if resume_drive:
    st.link_button("View Resume on Google Drive", resume_drive)

if not text:
    st.warning("No text loaded yet. Upload a PDF or configure resume_local_path in JSON.")
else:
    chunks = chunk_text(text, size=220)  # small chunks improve retrieval
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(chunks)

    q = st.text_input("Ask a question about my experience/projects/skills")
    if q:
        q_vec = vectorizer.transform([q])
        sims = cosine_similarity(q_vec, X)[0]
        top_idx = sims.argmax()
        answer = chunks[top_idx]
        st.markdown("### Answer (best matching snippet)")
        st.write(answer)
        st.caption(f"Similarity: {sims[top_idx]:.3f}")
