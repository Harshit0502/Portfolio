# app.py
import streamlit as st
from pathlib import Path
import base64

# ---------- BASIC CONFIG ----------
st.set_page_config(
    page_title="Harshit Mahour — Portfolio",
    page_icon="🧠",
    layout="wide"
)

# ---------- THEME HELPERS ----------
BADGE_CSS = """
<style>
.badge {display:inline-block;padding:.25rem .6rem;margin:.15rem;border-radius:999px;
        border:1px solid rgba(255,255,255,.25);font-size:.85rem; white-space:nowrap;}
hr {border: none; height: 1px; background: linear-gradient(90deg, #ccc0, #ccc5, #ccc0);}
.small {opacity:.8; font-size:.95rem}
.card {padding:1rem 1.1rem; border:1px solid rgba(255,255,255,.1); border-radius:14px; background:rgba(127,127,127,.06)}
.card h4 {margin:0 0 .25rem 0}
a {text-decoration: none}
</style>
"""
st.markdown(BADGE_CSS, unsafe_allow_html=True)

def badge(text):
    st.markdown(f"<span class='badge'>{text}</span>", unsafe_allow_html=True)

def file_download_button(label, file_path: Path):
    if file_path.exists():
        data = file_path.read_bytes()
        st.download_button(label, data=data, file_name=file_path.name, mime="application/pdf")
    else:
        st.info("Drop your resume PDF in this folder and set its name in the left sidebar.")
        st.button("Resume not found")

# ---------- SIDEBAR ----------
with st.sidebar:
    st.image(
        "https://avatars.githubusercontent.com/u/106897916?s=400",  # replace with your own image URL or local file
        caption="Harshit Mahour",
        use_container_width=True,
    )
    st.markdown("### Quick Links")
    st.markdown(
        """
- [LinkedIn](https://www.linkedin.com/in/harshit-mahour-6b760b213/)
- [GitHub](https://github.com/Harshit0502)
- [Codeforces](https://codeforces.com/profile/Harshit0502)
- [Cipher Shield (Live)](https://ciphershieldv3-kentdiwuszkthgk8bipobg.streamlit.app/)
        """
    )

    st.markdown("---")
    st.markdown("### Resume")
    resume_name = st.text_input("PDF filename", value="Harshit_Mahour_Resume.pdf")
    file_download_button("⬇️ Download Resume", Path(resume_name))

# ---------- HERO ----------
left, right = st.columns([2, 1], vertical_alignment="center")
with left:
    st.title("Harshit Mahour")
    st.subheader("Final-year CSE @ IIIT Bhopal • GenAI, NLP, Forecasting, MLOps")
    st.write(
        "I build **production-ready ML & GenAI systems** — from multimodal stock forecasters "
        "to secure NLP pipelines and real-time dashboards. Focused on **risk-aware AI** and "
        "**scalable deployments**."
    )
    cols = st.columns(5)
    with cols[0]: badge("Python")
    with cols[1]: badge("C++")
    with cols[2]: badge("TensorFlow")
    with cols[3]: badge("PyTorch")
    with cols[4]: badge("Docker • FastAPI • Streamlit")

with right:
    st.metric("Codeforces", "Specialist", delta="1484")
    st.metric("Internships", "Shell · IIT Bombay")
    st.metric("Focus", "GenAI • NLP • Forecasting")

st.markdown("---")

# ---------- EXPERIENCE ----------
st.header("Experience")
exp = [
    {
        "role": "AI/ML Intern — AICTE x Shell x Edunet Foundation",
        "time": "Jan 2025 – Feb 2025",
        "bullets": [
            "Designed ML pipelines (SVM, Ridge, RF) for sustainability analytics; **~18% R² uplift** on 15K records.",
            "Automated preprocessing/ETL with Pandas/NumPy; **~40% faster** handling.",
            "Built dashboards for 4+ mentorship reviews; interpretable visuals with Matplotlib/Seaborn."
        ],
    },
    {
        "role": "Software Fellow — FOSSEE, IIT Bombay (Osdag)",
        "time": "May 2025 – Jul 2025",
        "bullets": [
            "Optimized backend + PyQt5 GUI for a structural design tool used by **500+** academic users.",
            "Applied **PSO** to accelerate large-scale validation (**~30%** runtime cut).",
            "Refactored **800+ lines** into modular components; strengthened data governance & reproducibility."
        ],
    },
]
cols = st.columns(2)
for i, e in enumerate(exp):
    with cols[i % 2]:
        st.markdown(f"<div class='card'><h4>{e['role']}</h4><div class='small'>{e['time']}</div>", unsafe_allow_html=True)
        for b in e["bullets"]:
            st.markdown(f"- {b}")
        st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")

# ---------- PROJECTS ----------
st.header("Projects")
projects = [
    {
        "name": "Cipher Shield",
        "stack": "Django, Streamlit, Redis, AES-256, ECC, Docker, Scikit-learn",
        "links": {
            "GitHub": "https://github.com/Harshit0502/Cipher_Shield_V3_unDER_DEV",
            "Live": "https://ciphershieldv3-kentdiwuszkthgk8bipobg.streamlit.app/",
        },
        "highlights": [
            "Full-stack encrypted chat (AES-256, ECC, JWT) guarding against ransomware in unstructured chat.",
            "NLP anomaly detector (TF-IDF + Logistic Regression); **<250ms latency** at 10–20 concurrent users.",
            "**92% precision** in stress-tests for real-time governance."
        ],
    },
    {
        "name": "StockNews Engine — Multimodal Stock Movement Predictor",
        "stack": "TensorFlow, FAISS, C++, ONNX, Python",
        "links": {
            "GitHub": "https://github.com/Harshit0502/stock-news-engine",
        },
        "highlights": [
            "Fuses **news embeddings** with **OHLCV** data using multi-branch RNN/GRU/LSTM + Attention.",
            "Entropy-aware fusion + sentiment clustering; **68% crash-forecast accuracy (5-day)**.",
        ],
    },
]
for p in projects:
    st.markdown(f"#### {p['name']}")
    st.caption(p["stack"])
    cols = st.columns(2)
    with cols[0]:
        for h in p["highlights"]:
            st.markdown(f"- {h}")
    with cols[1]:
        for k, v in p["links"].items():
            st.markdown(f"- [{k}]({v})")
    st.markdown("")

st.markdown("---")

# ---------- RESEARCH ----------
st.header("Research (Working Paper)")
st.markdown(
    "- **“Risk-Aware Multimodal Forecasting with GenAI & NLP Models.”** "
    "Cascading architecture with graph links + entropy-aware fusion; improved crash prediction and governance alignment."
)

st.markdown("---")

# ---------- SKILLS ----------
st.header("Skills")
skill_cols = st.columns(3)
with skill_cols[0]:
    st.subheader("Programming")
    st.write("Python, C, C++")
    st.subheader("Data/ML")
    st.write("Scikit-learn, TensorFlow, PyTorch, XGBoost")
with skill_cols[1]:
    st.subheader("GenAI/NLP")
    st.write("HF Transformers, FAISS, LangChain, RAG, Sentence Embeddings")
    st.subheader("Databases")
    st.write("MySQL, MongoDB")
with skill_cols[2]:
    st.subheader("MLOps/Deploy")
    st.write("Docker, FastAPI, Streamlit, MLflow")
    st.subheader("CS Fundamentals")
    st.write("OOP, OS, CN (TCP/IP, routing)")

st.markdown("---")

# ---------- ACHIEVEMENTS ----------
st.header("Achievements")
ach_cols = st.columns(2)
with ach_cols[0]:
    st.markdown("- **Graph Camp 2024** — Selected from 80,000+; listed in Hall of Fame.")
    st.markdown("- **AtomQuest 2024** — Round 2 from 14K+, top ~2000.")
with ach_cols[1]:
    st.markdown("- **Codeforces** — Reached **1484 (Specialist)**, 100+ problems.")

st.markdown("---")

# ---------- EDUCATION ----------
st.header("Education")
st.markdown("**IIIT Bhopal** — B.Tech CSE (Nov 2022 – Jun 2026 expected)")
st.caption("Relevant Coursework: DS&A, DBMS, Computer Networks, Operating Systems, Distributed Systems")

# ---------- CONTACT ----------
st.markdown("---")
st.header("Contact")
st.write("📧 harshitmahour360@gmail.com &nbsp;|&nbsp; 📞 +91-9098509973")
st.write("Open to roles in **Software Engineering, Data Science, and GenAI**.")
