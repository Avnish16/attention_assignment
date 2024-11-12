import streamlit as st
import requests

st.title("Academic Research Paper Assistant")

# Topic input
topic = st.text_input("Enter a research topic")

if st.button("Search Papers"):
    response = requests.get(f"http://localhost:8000/search?topic={topic}")
    papers = response.json().get("papers", [])
    for paper in papers:
        st.write(f"**Title**: {paper['title']}")
        st.write(f"**Abstract**: {paper['abstract']}")

# For generating future research ideas
if st.button("Generate Future Research Directions"):
    context = "\n".join([paper['abstract'] for paper in papers])
    response = requests.get(f"http://localhost:8000/future_works?context={context}")
    st.write(response.json()["future_works"])
