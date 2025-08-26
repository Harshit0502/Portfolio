import streamlit as st
st.markdown(f"### {data.get('name','Your Name')}")
st.caption(data.get("role", "Role"))
st.write(data.get("summary", ""))
# socials
if data.get("socials"):
for k, v in data["socials"].items():
st.link_button(k, v, use_container_width=True)
if data.get("resume_url"):
st.link_button("Download Resume", data["resume_url"], use_container_width=True)


st.title("👋 Welcome")
st.write("Use the left sidebar to navigate pages. This home page mirrors highlights from your JSON.")


# Highlights grid
col1, col2 = st.columns([1.1, 2])
with col1:
st.subheader("About")
st.write(data.get("summary", ""))
contact = data.get("contact", {})
st.write(f"**Email:** {contact.get('email','')} ")
st.write(f"**Location:** {contact.get('location','')}")
with col2:
st.subheader("Quick Links")
links = data.get("quick_links", [])
if links:
for item in links:
st.markdown(f"- [{item['title']}]({item['url']})")
else:
st.info("Add quick_links in data/portfolio.json to show items here.")


st.divider()


st.subheader("Featured Projects")
projects = data.get("projects", [])[:2]
if not projects:
st.info("Add projects in data/portfolio.json to feature here.")
else:
for p in projects:
c1, c2 = st.columns([1.1, 2])
with c1:
img = load_image(p.get("image", ""))
if img: st.image(img, use_column_width=True)
st.markdown("**Tech**: " + ", ".join(p.get("stack", [])))
if p.get("links"):
st.markdown('<div class="btn-row">' + " ".join(
[f"<a href='{u}' target='_blank'>🔗 {k}</a>" for k, u in p["links"].items()]
) + "</div>", unsafe_allow_html=True)
with c2:
st.markdown(f"**{p.get('title','')}**")
st.write(p.get("summary", ""))
for h in p.get("highlights", []):
st.markdown(f"- {h}")
st.markdown("---")
