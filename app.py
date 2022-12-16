import streamlit as st

st.set_page_config(
    page_title="Salary_Predictor",
    page_icon="random"
)


from predict_page import show_predict_page
from explore_page import show_explore_page
page = st.sidebar.selectbox("Predict or Explore", ("Predict", "Explore"))

if page == "Predict":
    show_predict_page()
else:
    show_explore_page()
