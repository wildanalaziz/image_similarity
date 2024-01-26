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

    # col3, col4 = st.columns(2)
    # if origin is not None:
    #     origin_fg = rembg.remove(Image.open(origin))
    #     with col3:
    #         st.image(origin_fg, caption="Origin Photo")
    # if arrival is not None:
    #     arrival_fg = rembg.remove(Image.open(arrival))
    #     with col4:
    #         st.image(rembg.remove(arrival_fg), caption="Arrival Photo")