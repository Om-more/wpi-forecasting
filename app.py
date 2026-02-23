import streamlit as st
import pandas as pd
import pickle
from pathlib import Path

BASE_DIR = Path(__file__).parent

MODEL_PATH = BASE_DIR / "all_crop_models.pkl"

CROP_DATA_FILES = {
    "masur": BASE_DIR / "Masur_data.csv",
    "bajra": BASE_DIR / "Bajra_data.csv",
    "moong": BASE_DIR / "Moong_data.csv",
    "cauliflower": BASE_DIR / "Cauliflower_data.csv",
}

st.set_page_config(
    page_title="WPI Forecasting Dashboard",
    layout="wide"
)

st.title("Wholesale Price Index Forecasting")


@st.cache_resource
def load_models():
    with open(MODEL_PATH, "rb") as f:
        models = pickle.load(f)
    return models

if not MODEL_PATH.exists():
    st.error("all_crop_models.pkl not found.")
    st.stop()

models = load_models()
st.sidebar.header("Controls")

available_crops = (models.keys())

selected_crop = st.sidebar.selectbox(
    "Select Commodity",
    available_crops
)

forecast_months = st.sidebar.slider(
    "Forecast Horizon (months)",
    min_value=6,
    max_value=24,
    value=12
)

@st.cache_data
def load_crop_data(csv_path):
    df = pd.read_csv(csv_path)
    df["ds"] = pd.to_datetime(df["ds"])
    return df

if selected_crop not in CROP_DATA_FILES:
    st.error(f"No CSV file mapped for {selected_crop}")
    st.stop()

csv_path = CROP_DATA_FILES[selected_crop]

if not csv_path.exists():
    st.error(f"Data file not found: {csv_path.name}")
    st.stop()

df = load_crop_data(csv_path)

# Expecting columns: ds, y
if not {"ds", "y"}.issubset(df.columns):
    st.error("CSV must contain columns: ds, y")
    st.stop()

df = df.dropna()
last_date = df["ds"].max()

st.subheader(f"Historical WPI: {selected_crop}")

st.line_chart(
    df.set_index("ds")["y"]
)

st.caption(f"Last available data: **{last_date.date()}**")

model = models[selected_crop]

future = model.make_future_dataframe(
    periods=forecast_months,
    freq="M"
)

forecast = model.predict(future)

future_forecast = forecast[forecast["ds"] > last_date][
    ["ds", "yhat", "yhat_lower", "yhat_upper"]
]

st.subheader("Forecast")
fig1 = model.plot(forecast)
st.pyplot(fig1)
st.subheader("Trend & Seasonality")

fig2 = model.plot_components(forecast)
st.pyplot(fig2)

st.subheader("Forecast Values")

st.dataframe(
    future_forecast.style.format({
        "yhat": "{:.2f}",
        "yhat_lower": "{:.2f}",
        "yhat_upper": "{:.2f}",
    })
)

csv = future_forecast.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download Forecast CSV",
    data=csv,
    file_name=f"{selected_crop}_forecast.csv",
    mime="text/csv"
)

st.caption(
    "Note: WPI data is published with a delay and the most recent values may be provisional. "
    "Forecasts are forward-looking estimates based on historical trends and seasonality."
)
