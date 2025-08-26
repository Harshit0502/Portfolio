import streamlit as st
import json
from pathlib import Path

st.set_page_config(page_title="Experience — Harshit Mahour", page_icon="💼", layout="wide")
DATA_PATH = Path("data/portfolio.json")

@st.cache_data
def load_data():
    return json.loads(DATA_PATH.read_text(encoding="utf-8"))

st.title("💼 Experience")

data = load_data()
exp = data.get("experience", [])
if not exp:
    st.info("Add experience in data/portfolio.json")
else:
    for e in exp:
        st.markdown(f"**{e['role']}** · {e['company']}  \\n*{e['dates']}*")
        for b in e.get("bullets", []):
            st.markdown(f"- {b}")
        st.markdown("")

st.subheader("🎓 Education")
edu = data.get("education", [])
for ed in edu:
    st.markdown(f"**{ed['school']}** — {ed['degree']}  \\n*{ed['dates']}*")
    if ed.get("coursework"): st.caption(", ".join(ed["coursework"]))
