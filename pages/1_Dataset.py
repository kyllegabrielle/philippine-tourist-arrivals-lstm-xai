
import streamlit as st
import pandas as pd
from pathlib import Path
from styles import apply_custom_css

apply_custom_css()

st.title("1. Dataset summary")

if "raw_df" not in st.session_state:
    st.session_state.raw_df = (
        pd.read_csv(
            Path(__file__).resolve().parents[1] / "data" / "tourist_arrivals.csv",
            # This CSV has two title rows before the actual column names.
            skiprows=2,
            parse_dates=["date"]
        )
        .sort_values("date")
        .reset_index(drop=True)
    )

df = st.session_state.raw_df

st.write(f"{len(df)} rows, {len(df.columns)} columns")
st.dataframe(df.head())

expected = pd.date_range(
    df["date"].min(),
    df["date"].max(),
    freq="MS"
)

missing_months = expected.difference(df["date"])

if len(missing_months):
    st.warning(f"Missing months: {list(missing_months)}")
else:
    st.success("No gaps in the monthly sequence.")
