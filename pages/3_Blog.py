import streamlit as st
import feedparser
import json
from pathlib import Path

st.set_page_config(page_title="Blog — Harshit Mahour", page_icon="📰", layout="wide")
DATA_PATH = Path("data/portfolio.json")

@st.cache_data
def load_data():
    return json.loads(DATA_PATH.read_text(encoding="utf-8"))

@st.cache_data(ttl=3600)
def fetch_rss(url: str, limit: int = 5):
    if not url: return []
    feed = feedparser.parse(url)
    items = []
    for e in feed.entries[:limit]:
        items.append({
            "title": getattr(e, 'title', ''),
            "link": getattr(e, 'link', ''),
            "date": getattr(e, 'published', getattr(e, 'updated', '')),
        })
    return items

st.title("📰 Latest Updates")

data = load_data()
rss_url = data.get("blog", {}).get("rss_url", "")
if not rss_url:
    st.info("Add blog.rss_url in data/portfolio.json")
else:
    posts = fetch_rss(rss_url)
    if not posts:
        st.warning("No recent posts found.")
    else:
        for p in posts:
            st.markdown(f"**[{p['title']}]({p['link']})**  ")
            st.caption(p.get("date", ""))
            st.markdown("---")
