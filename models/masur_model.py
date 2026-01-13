from data_filter import clean_df
import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt

prophet_df_3 = clean_df[['ds','Masur']].rename(columns={'Masur': 'y'})

train_3 = prophet_df_3[prophet_df_3['ds'] < '2022-01-01']
test_3 = prophet_df_3[(prophet_df_3['ds'] >= '2022-01-01') & (prophet_df_3['ds'] < '2023-01-01')]

model_3 = Prophet(
    yearly_seasonality=True,
    weekly_seasonality=False,
    daily_seasonality=False
)

model_3.fit(train_3)
future_3 = model_3.make_future_dataframe(periods=24, freq='ME')
forecast_3= model_3.predict(future_3)

fig1 = model_3.plot(forecast_3)
fig1.savefig("forecast_plot_3.png", dpi=300, bbox_inches="tight")
plt.close(fig1)
fig2 = model_3.plot_components(forecast_3)
fig2.savefig("components_plot_3.png", dpi=300, bbox_inches="tight")
plt.close(fig2)