import streamlit as st
import similiarity

st.sidebar.header("Sarana Machine Learning")

origin = st.sidebar.file_uploader("Origin Photo", type=["jpg", "jpeg"])
arrival = st.sidebar.file_uploader("Arrival Photo", type=["jpg", "jpeg"])

proses = st.sidebar.button("Check Similarity")
if proses:
    similarity_score = similiarity.get_similarity_score(origin, arrival)
    st.title("Similarity Score")
    st.header(similarity_score[0])

    col1, col2 = st.columns(2)
    if origin is not None:
        with col1:
            st.image(origin, caption="Origin Photo")
    if arrival is not None:
        with col2:
            st.image(arrival, caption="Arrival Photo")