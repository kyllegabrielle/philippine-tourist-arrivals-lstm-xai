# pages/5_Train.py
import streamlit as st
import itertools
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Input, LSTM, Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping

st.title("5. Train and tune the LSTM")

if "X_train_seq" not in st.session_state:
    st.warning("Run the Prepare page first.")
    st.stop()

PARAM_GRID = {"units": [32, 64], "dropout": [0.1, 0.3], "batch_size": [16, 32]}

if st.button("Train & tune"):
    X_train = np.asarray(st.session_state.X_train_seq, dtype=np.float32)
    y_train = np.asarray(st.session_state.y_train_seq, dtype=np.float32)

    if X_train.ndim != 3 or y_train.shape[0] != X_train.shape[0]:
        st.error("The prepared training sequences are invalid. Run the Prepare page again.")
        st.stop()

    # Missing values in the CSV can produce invalid sequence inputs or
    # targets. TensorFlow trains on NaNs without raising an exception, which
    # makes every validation loss NaN and leaves no best model to select.
    valid_rows = np.isfinite(X_train).all(axis=(1, 2))
    valid_rows &= np.isfinite(y_train.reshape(y_train.shape[0], -1)).all(axis=1)
    skipped_rows = int((~valid_rows).sum())
    X_train = X_train[valid_rows]
    y_train = y_train[valid_rows]

    if len(X_train) < 10:
        st.error("Too few valid training sequences remain. Check missing values and run Prepare again.")
        st.stop()

    with st.spinner("Training… this can take a while"):
        lookback = X_train.shape[1]
        n_features = X_train.shape[2]
        best_val_loss, best_params, best_model, best_history = float("inf"), None, None, None

        for units, dropout, batch_size in itertools.product(*PARAM_GRID.values()):
            candidate = Sequential([
                Input(shape=(lookback, n_features)),
                LSTM(units),
                Dropout(dropout),
                Dense(1),
            ])
            candidate.compile(optimizer="adam", loss="mse")
            hist = candidate.fit(
                X_train, y_train,
                validation_split=0.15, epochs=100, batch_size=batch_size,
                callbacks=[EarlyStopping(patience=8, restore_best_weights=True)],
                verbose=0,
            )
            finite_val_losses = [loss for loss in hist.history["val_loss"] if np.isfinite(loss)]
            if not finite_val_losses:
                continue
            val_loss = min(finite_val_losses)
            if val_loss < best_val_loss:
                best_val_loss = val_loss
                best_params = {"units": units, "dropout": dropout, "batch_size": batch_size}
                best_model, best_history = candidate, hist.history

    if best_model is None:
        st.error("Training did not produce a finite validation loss. Run Clean and Prepare again.")
        st.stop()

    st.session_state.model = best_model  # used by every later page
    st.session_state.train_report = {
        "best_params": best_params,
        "val_loss": best_val_loss,
        "loss_history": best_history["loss"],
        "val_loss_history": best_history["val_loss"],
        "skipped_rows": skipped_rows,
    }

# Displayed outside the button block, so the result is still here if you
# leave this page and come back.
if "train_report" in st.session_state:
    r = st.session_state.train_report
    st.success(f"Best hyperparameters: {r['best_params']} (val_loss = {r['val_loss']:.4f})")
    if r.get("skipped_rows", 0):
        st.info(f"Skipped {r['skipped_rows']} training sequences containing missing values.")
    st.line_chart({"loss": r["loss_history"], "val_loss": r["val_loss_history"]})
else:
    st.info('Click "Train & tune" to fit the LSTM on the sequences from the Prepare page.')
