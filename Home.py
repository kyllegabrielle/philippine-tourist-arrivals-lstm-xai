import streamlit as st
from styles import apply_custom_css

st.set_page_config(
    page_title="Tourist Arrivals Forecast",
    page_icon="✈️",
    layout="wide"
)

apply_custom_css()

st.title("Philippine Tourist Arrivals")
st.caption("Forecasting with LSTM & Explainable AI")

st.write(
    "Explore Philippine tourist arrivals through "
    "historical data, climate factors, machine learning, "
    "and explainable forecasting."
)

st.divider()
st.subheader("Explore the forecasting pipeline")
st.write(
    "Use the sidebar to navigate through the eight stages "
    "of the forecasting process, starting with Dataset "
    "and ending with Forecast."
)
