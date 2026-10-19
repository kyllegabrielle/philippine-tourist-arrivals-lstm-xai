# Philippine Tourist Arrivals Forecasting with LSTM & XAI

A Python-based Streamlit application that forecasts monthly tourist arrivals in the Philippines using a Long Short-Term Memory (LSTM) model. It also uses SHAP (SHapley Additive exPlanations) to help explain which input features influence the model's predictions.

This project was developed for **Laboratory Exercise 1 — Forecasting Philippine Tourist Arrivals with LSTM & XAI**.

## Features

The application includes eight pages that guide users through the forecasting process:

1. **Dataset** — Loads the tourist arrivals dataset, previews records, and checks for missing months.
2. **Clean** — Checks duplicate records, missing values, and possible outliers.
3. **Features** — Selects predictors using Spearman correlation and Variance Inflation Factor (VIF).
4. **Prepare** — Splits data chronologically, scales the features, and creates sequences for the LSTM model.
5. **Train** — Trains an LSTM model and tunes its hyperparameters using validation data.
6. **Evaluate** — Reports MAE, RMSE, MAPE, and R², and compares the LSTM against naive and seasonal-naive forecasts.
7. **Explain** — Uses SHAP to display feature importance and explain model predictions.
8. **Forecast** — Lets users adjust input readings and generate a tourist arrivals prediction.

## Technologies Used

- **Python** — Application and model development
- **Streamlit** — Web interface
- **Pandas and NumPy** — Data processing
- **SciPy and Statsmodels** — Spearman correlation and VIF
- **Scikit-learn** — Data scaling and evaluation support
- **TensorFlow / Keras** — LSTM forecasting model
- **SHAP** — Model explainability

## Project Structure

```text
tourist-arrivals-app/
├── data/
│   └── tourist_arrivals.csv
├── pages/
│   ├── 1_Dataset.py
│   ├── 2_Clean.py
│   ├── 3_Features.py
│   ├── 4_Prepare.py
│   ├── 5_Train.py
│   ├── 6_Evaluate.py
│   ├── 7_Explain.py
│   └── 8_Forecast.py
├── Home.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/philippine-tourist-arrivals-lstm-xai.git
cd philippine-tourist-arrivals-lstm-xai
```

Replace `YOUR-USERNAME` with your GitHub username.

### 2. Create a virtual environment

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows (PowerShell):**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Add the dataset

Place `tourist_arrivals.csv` inside the `data/` folder if it is not already included in the repository. Use the dataset supplied for the laboratory exercise.

### 5. Run the application

```bash
python -m streamlit run Home.py
```

Open **http://localhost:8501** in your browser if it does not open automatically.

## How to Use

1. Open **Dataset** to load and inspect the monthly records.
2. Go to **Clean** and run the data checks.
3. Open **Features** to select relevant predictors.
4. Go to **Prepare** to create the training and testing sequences.
5. Open **Train** to train and tune the LSTM model.
6. Check **Evaluate** to review the model's performance.
7. Open **Explain** to inspect the SHAP results.
8. Go to **Forecast** to edit the available input readings and generate a prediction.

**Note:** Follow the pages in order. This implementation stores intermediate results and the trained model in Streamlit session state, so restarting the app or clearing the session may require running the steps again.

## Notes

- The dataset contains monthly tourist arrivals alongside calendar, climate, and hazard-related variables.
- Model performance depends on the dataset, selected features, training settings, and test period.
- SHAP explanations describe the model's behavior; they do not establish cause-and-effect relationships.
- Forecasts are estimates and should not be treated as guaranteed tourist arrival counts.

## Laboratory Submission

- **GitHub Repository:** Add your repository link here.
- **Demo Video (maximum 3 minutes):** Add your video link here.

## Acknowledgment

Developed as part of a laboratory exercise on time-series forecasting and explainable artificial intelligence (XAI).
