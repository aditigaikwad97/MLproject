from sklearn.preprocessing import LabelEncoder
from predict_page import show_predict_page
import streamlit as st

st.sidebar.selectbox("Explore or Predict",("Explore","Predict"))
show_predict_page()


