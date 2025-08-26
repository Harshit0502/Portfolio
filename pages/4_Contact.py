import streamlit as st
import json
from pathlib import Path

st.set_page_config(page_title="Contact — Harshit Mahour", page_icon="✉️", layout="wide")
DATA_PATH = Path("data/portfolio.json")

@st.cache_data
def load_data():
    return json.loads(DATA_PATH.read_text(encoding="utf-8"))

st.title("✉️ Contact")

data = load_data()
email_to = data.get("contact", {}).get("email", "")

with st.form("contact_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    msg = st.text_area("Message")
    ok = st.form_submit_button("Send Message")
    if ok:
        if not (name and email and msg):
            st.error("Please fill all fields.")
        else:
            st.success("Thanks! I'll get back to you soon.")
            if email_to:
                st.markdown(f"[📧 Email fallback](mailto:{email_to}?subject=Hello%20from%20{name}&body={msg})")

st.info("Prefer DM? See social links in the sidebar.")
