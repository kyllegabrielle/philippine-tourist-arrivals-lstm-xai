# pages/3_Features.py
import streamlit as st
import pandas as pd
from scipy.stats import spearmanr
from statsmodels.stats.outliers_influence import variance_inflation_factor

st.title("3. Feature selection")

if "clean_df" not in st.session_state:
    st.warning("Run the Clean page first.")
    st.stop()

# season and monsoon carry real seasonal signal but are text categories, not
# numbers — Spearman correlation can't be computed on them directly. Encode
# them into their own numeric columns in Clean.py's cleaning step, then add
# those column names here alongside the rest.
CANDIDATES = [
    "quarter", "is_holiday_peak", "temp_mean_c", "temp_min_c", "temp_max_c",
    "rainfall_mm", "rainy_days", "humidity_pct", "typhoon_count",
    "typhoon_max_wind_kt", "storm_signal_days", "pm25_ugm3", "wave_height_m",
]

if st.button("Run Spearman + VIF"):
    df = st.session_state.clean_df.copy()

    if "arrivals" not in df.columns:
        st.error("The cleaned dataset has no 'arrivals' column. Run the Dataset and Clean pages again.")
        st.stop()

    # Work only with columns that are present in the CSV. This also lets the
    # page continue if optional weather columns are removed from the file.
    available_candidates = [col for col in CANDIDATES if col in df.columns]
    missing_candidates = [col for col in CANDIDATES if col not in df.columns]

    if not available_candidates:
        st.error("The cleaned dataset has no numeric feature columns to analyze.")
        st.stop()

    numeric_df = df[available_candidates + ["arrivals"]].apply(
        pd.to_numeric, errors="coerce"
    )

    # Step 1 — univariate filter
    results = []
    for col in available_candidates:
        pair = numeric_df[[col, "arrivals"]].dropna()
        if len(pair) < 3 or pair[col].nunique() < 2:
            rho, p_value = float("nan"), float("nan")
        else:
            rho, p_value = spearmanr(pair[col], pair["arrivals"])
        results.append({"feature": col, "rho": rho, "p_value": p_value})
    kept = [r["feature"] for r in results if abs(r["rho"]) > 0.10 and r["p_value"] < 0.05]

    # Step 2 — iterative VIF
    X = numeric_df[kept].dropna()
    vif_log = []
    while X.shape[1] > 1:
        vifs = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
        max_vif = max(vifs)
        if max_vif < 5:
            break
        drop_col = X.columns[vifs.index(max_vif)]
        vif_log.append({"dropped": drop_col, "vif": max_vif})
        X = X.drop(columns=[drop_col])

    st.session_state.selected_features = list(X.columns)  # used by every later page
    st.session_state.feature_report = {
        "results": results,
        "vif_log": vif_log,
        "missing_candidates": missing_candidates,
    }

# Displayed outside the button block, so the result is still here if you
# leave this page and come back.
if "feature_report" in st.session_state:
    report = st.session_state.feature_report
    st.dataframe(report["results"])
    if report.get("missing_candidates"):
        st.info(f"Skipped columns not found in the CSV: {report['missing_candidates']}")
    st.write("VIF removals:", report["vif_log"])
    selected = st.session_state.get("selected_features", [])
    if selected:
        st.success(f"Selected features: {selected}")
    else:
        st.warning("No features passed the Spearman correlation filter.")
else:
    st.info('Click "Run Spearman + VIF" to select features from the cleaned dataset.')
