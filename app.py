from sklearn.preprocessing import LabelEncoder
from predict_page import show_predict_page
from explore_page import show_explore_page
import streamlit as st

page = st.sidebar.selectbox("Explore or Predict",("Explore","Predict"))

if page == "Predict":
    show_predict_page()
else:
    show_explore_page()


