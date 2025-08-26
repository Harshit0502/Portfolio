import streamlit as st
from PIL import Image
from io import BytesIO
import base64
import textwrap

# -------------- PAGE CONFIG --------------
st.set_page_config(
    page_title="Harshit Mahour — Portfolio",
    page_icon="🤖",
    layout="wide"
)

# -------------- THEME TOGGLE --------------
if "theme" not in st.session_state:
    st.session_state.theme = "light"
def toggle_theme():
    st.session_state.theme = "dark" if st.session_state.theme == "light" else "light"
with st.sidebar:
    st.markdown("## 🎨 Theme")
    st.button(f"Switch to {'🌙 Dark' if st.session_state.theme=='light' else '☀️ Light'}", on_click=toggle_theme)
    st.markdown("---")

# -------------- DATA (EDIT ME) --------------
PROFILE = {
    "name": "Harshit Mahour",
    "role": "Final-year CSE @ IIIT Bhopal | GenAI • NLP • Data Science",
    "pitch": "Built scalable ML pipelines, multimodal stock forecasting engines, and secure NLP systems. Focused on GenAI/NLP for unstructured data and risk-aware forecasting.",
    "location": "India",
    "email": "harshitmahour360@gmail.com",
    "phone": "+91 9098509973",
    "socials": {
        "LinkedIn": "https://www.linkedin.com/in/harshit-mahour-6b760b213/",
        "GitHub": "https://github.com/Harshit0502",
        "Codeforces": "https://codeforces.com/profile/Harshit0502"
    },
    # Your Google Drive resume link (given by you)
    "resume_url": "https://drive.google.com/file/d/1vdg17u8q0HZdD0JdWJWbvhnu3nMlGQRg/view?usp=sharing",
    # Optional local assets (put files under ./assets and update paths)
    "avatar_path": "assets/avatar.jpg",  # keep placeholder; shows fallback if missing
}

SKILLS = {
    "Programming": ["Python", "C", "C++"],
    "Data Science & ML": ["scikit-learn", "TensorFlow", "PyTorch", "XGBoost"],
    "GenAI & NLP": ["Transformers", "FAISS", "LangChain", "RAG", "Sentence Embeddings"],
    "MLOps & Deploy": ["Docker", "FastAPI", "Streamlit", "MLflow"],
    "Databases": ["MySQL", "MongoDB"],
    "CS Fundamentals": ["OOP", "OS", "Computer Networks (TCP/IP, routing)"],
    "Problem Solving": ["Data Structures & Algorithms", "Competitive Programming (CF Specialist 1484)"]
}

PROJECTS = [
    {
        "title": "Cipher Shield",
        "summary": "Full-stack encrypted chat platform with AES-256, ECC, JWT + NLP-based anomaly detection.",
        "stack": ["Django", "Streamlit", "Redis", "AES", "ECC", "Scikit-learn", "Docker"],
        "links": {
            "GitHub": "https://github.com/Harshit0502/Cipher_Shield_V3_unDER_DEV",
            "Live": "https://ciphershieldv3-kentdiwuszkthgk8bipobg.streamlit.app/"
        },
        "highlights": [
            "92% detection precision with <250ms latency (10–20 concurrent users).",
            "Real-time governance of unstructured data streams."
        ],
        "image": "assets/ciphershield.png",
        "alt": "Cipher Shield app screenshot"
    },
    {
        "title": "StockNews Engine — Multimodal Stock Movement Predictor",
        "summary": "Integrates financial news embeddings with OHLCV to capture event-driven risks; multi-branch NN with entropy-aware fusion.",
        "stack": ["TensorFlow", "FAISS", "C++", "ONNX", "Python"],
        "links": {
            "GitHub": "https://github.com/Harshit0502/stock-news-engine"
        },
        "highlights": [
            "Crash forecast accuracy: 68% @ 5-day horizon (backtests).",
        ],
        "image": "assets/stocknews.png",
        "alt": "StockNews Engine charts"
    }
]

EXPERIENCE = [
    {
        "company": "FOSSEE, IIT Bombay (Osdag)",
        "role": "Software Fellow",
        "dates": "May 2025 – Jul 2025",
        "bullets": [
            "Optimized backend + GUI (Python, PyQt5) for a structural design tool used by 500+ academic users.",
            "Applied PSO optimization ⇒ 30% faster large-scale data validation.",
            "Refactored 800+ LOC into modular components; improved QA integration."
        ]
    },
    {
        "company": "AICTE × Shell × Edunet Foundation",
        "role": "AI/ML Intern",
        "dates": "Jan 2025 – Feb 2025",
        "bullets": [
            "Evaluated SVM/Ridge/RF pipelines for sustainability analytics on 15K records (↑ ~18% R²).",
            "Automated ETL with Pandas/NumPy (↓ 40% handling time).",
            "Built interpretable dashboards (Matplotlib/Seaborn) for 4+ mentorship reviews."
        ]
    }
]

EDUCATION = [
    {
        "school": "IIIT Bhopal",
        "degree": "B.Tech, Computer Science & Engineering",
        "dates": "Nov 2022 – Jun 2026 (Expected)",
        "coursework": ["DSA", "DBMS", "Computer Networks", "Operating Systems", "Distributed Systems"]
    }
]

ACHIEVEMENTS = [
    "Graph Camp 2024 — selected from 80,000+ applicants; Hall of Fame recognition.",
    "AtomQuest 2024 — Round 2 (top ~2000 of 14K+).",
    "Codeforces Specialist — max rating 1484 (100+ problems)."
]

# Add any other personal links here (drive papers, demos, etc.)
OTHER_LINKS = [
    # Examples from your resume footer:
    "https://drive.google.com/file/d/1awOflMD2lI0cfJPbqI9cv9nrOkz6ig8_/view",
    "https://drive.google.com/file/d/17iNhG62Try2ujCYAyl2B_EV-lmu0vwxT/view?usp=sharing",
    "https://drive.google.com/file/d/10kJ30Q9q0OXltdNnhFI98uf3NIWSPoSt/view?usp=sharing"
]

# -------------- HELPERS --------------
def load_image(path: str):
    try:
        return Image.open(path)
    except Exception:
        return None

def badge(text: str):
    return f"<span style='padding:4px 8px;border-radius:999px;border:1px solid var(--text-color);font-size:0.85rem;white-space:nowrap;display:inline-block;margin:2px 6px 2px 0;'>{text}</span>"

def apply_theme():
    if st.session_state.theme == "dark":
        st.markdown("""
        <style>
        :root { --text-color: #EAEAEA; --muted: #A7A7A7; }
        .stApp { background:#0f1116; color:var(--text-color); }
        .st-emotion-cache-16txtl3, .st-emotion-cache-1kyxreq { color: var(--text-color) !important; }
        hr { border-color:#333; }
        </style>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <style>
        :root { --text-color: #111; --muted: #555; }
        .stApp { background:#ffffff; color:var(--text-color); }
        hr { border-color:#eaeaea; }
        </style>
        """, unsafe_allow_html=True)

apply_theme()

# -------------- HERO --------------
left, right = st.columns([1, 2.2], vertical_alignment="center")

with left:
    avatar = load_image(PROFILE["avatar_path"])
    if avatar:
        st.image(avatar, caption="", use_column_width=True)
    else:
        st.markdown("🧑‍💻")

with right:
    st.markdown(f"### {PROFILE['name']}")
    st.markdown(f"**{PROFILE['role']}**")
    st.write(PROFILE["pitch"])
    cols = st.columns(len(PROFILE["socials"]) + 1)
    idx = 0
    for k, v in PROFILE["socials"].items():
        with cols[idx]:
            st.link_button(k, v, use_container_width=True)
        idx += 1
    with cols[idx]:
        st.link_button("Resume", PROFILE["resume_url"], use_container_width=True)

st.divider()

# -------------- ABOUT + SKILLS --------------
st.subheader("About")
about_cols = st.columns(3)
about_cols[0].metric("Location", PROFILE["location"])
about_cols[1].metric("Email", PROFILE["email"])
about_cols[2].metric("Phone", PROFILE["phone"])

st.write(
    "I design data/ML systems that move from **prototype → production** cleanly: "
    "pipelines, ETL, MLOps, dashboards, and research-backed GenAI features."
)

st.markdown("#### Skills")
for cat, items in SKILLS.items():
    st.markdown(f"**{cat}**", help=cat)
    st.markdown("".join([badge(x) for x in items]), unsafe_allow_html=True)

st.divider()

# -------------- PROJECTS --------------
st.subheader("Projects")
for p in PROJECTS:
    c1, c2 = st.columns([1.1, 2.2])
    with c1:
        img = load_image(p["image"])
        if img:
            st.image(img, caption=p.get("alt",""), use_column_width=True)
        else:
            st.markdown("🧩 (image placeholder)")
        st.markdown("**Tech**: " + ", ".join(p["stack"]))
        if p.get("links"):
            link_cols = st.columns(len(p["links"]))
            i = 0
            for lk, url in p["links"].items():
                with link_cols[i]:
                    st.link_button(lk, url, use_container_width=True)
                i += 1
    with c2:
        st.markdown(f"**{p['title']}**")
        st.write(p["summary"])
        if p.get("highlights"):
            st.markdown("- " + "\n- ".join(p["highlights"]))
    st.markdown("---")

# -------------- EXPERIENCE --------------
st.subheader("Experience")
for item in EXPERIENCE:
    st.markdown(f"**{item['role']}** · {item['company']}  \n*{item['dates']}*")
    for b in item["bullets"]:
        st.markdown(f"- {b}")
    st.markdown("")

# -------------- EDUCATION --------------
st.subheader("Education")
for edu in EDUCATION:
    st.markdown(f"**{edu['school']}** — {edu['degree']}  \n*{edu['dates']}*")
    if edu.get("coursework"):
        st.markdown("**Relevant Coursework:** " + ", ".join(edu["coursework"]))
    st.markdown("")

# -------------- ACHIEVEMENTS --------------
st.subheader("Achievements")
for a in ACHIEVEMENTS:
    st.markdown(f"- {a}")

# -------------- OTHER LINKS --------------
if OTHER_LINKS:
    st.subheader("Other Links")
    for url in OTHER_LINKS:
        st.write(f"- {url}")

st.divider()

# -------------- CONTACT FORM --------------
st.subheader("Contact")
with st.form("contact"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    msg = st.text_area("Message")
    submitted = st.form_submit_button("Send")
    if submitted:
        if not name or not email or not msg:
            st.error("Please fill all fields.")
        else:
            st.success("Thanks! I’ll get back to you soon.")
            mailto = f"mailto:{PROFILE['email']}?subject=Portfolio%20Contact%20from%20{name}&body={msg}"
            st.markdown(f"[📧 Email fallback]({mailto})")

# -------------- README / HOW TO RUN --------------
with st.expander("How to run / Deploy"):
    st.markdown("""
**Local**
1. Create venv & install requirements:  
   ```bash
   pip install -r requirements.txt
