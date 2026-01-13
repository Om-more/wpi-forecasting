from data_filter import clean_df
import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt

prophet_df_2 = clean_df[['ds','Moong']].rename(columns={'Moong': 'y'})
train_2 = prophet_df_2[prophet_df_2['ds'] < '2022-01-01']
test_2 = prophet_df_2[(prophet_df_2['ds'] >= '2022-01-01') & (prophet_df_2['ds'] < '2023-01-01')]
from prophet import Prophet

model_2 = Prophet(
    yearly_seasonality=True,
    weekly_seasonality=False,
    daily_seasonality=False
)

model_2.fit(train_2)
future_2 = model_2.make_future_dataframe(periods=24, freq='ME')
forecast_2= model_2.predict(future_2)

fig1 = model_2.plot(forecast_2)
fig1.savefig("forecast_plot_2.png", dpi=300, bbox_inches="tight")
plt.close(fig1)
fig2 = model_2.plot_components(forecast_2)
fig2.savefig("components_plot_2.png", dpi=300, bbox_inches="tight")
plt.close(fig2)
