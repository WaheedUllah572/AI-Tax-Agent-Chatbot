import streamlit as st

st.title("📄 Test File Upload")

file = st.file_uploader("Upload a PDF", type=["pdf"])

if file:
    st.write("File uploaded:", file.name)
