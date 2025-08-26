import streamlit as st
from PIL import Image
import json
from pathlib import Path

st.set_page_config(page_title="Projects — Harshit Mahour", page_icon="🧩", layout="wide")
DATA_PATH = Path("data/portfolio.json")

@st.cache_data
def load_data():
    return json.loads(DATA_PATH.read_text(encoding="utf-8"))

def load_image(path: str):
    try:
        return Image.open(path)
    except Exception:
        return None

st.title("🧩 Projects")

data = load_data()
projects = data.get("projects", [])
if not projects:
    st.info("No projects found in data/portfolio.json")
else:
    for p in projects:
        with st.container():
            c1, c2 = st.columns([1.1, 2])
            with c1:
                img = load_image(p.get("image", ""))
                if img: st.image(img, use_column_width=True)
                st.markdown("**Tech**: " + ", ".join(p.get("stack", [])))
                links = p.get("links", {})
                link_cols = st.columns(len(links)) if links else []
                for i, (k, u) in enumerate(links.items()):
                    with link_cols[i]:
                        st.link_button(k, u, use_container_width=True)
            with c2:
                st.markdown(f"### {p.get('title','')}")
                st.write(p.get("summary", ""))
                if p.get("highlights"):
                    st.markdown("- " + "\n- ".join(p["highlights"]))
            st.markdown("---")
