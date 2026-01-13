from data_filter import clean_df
import pandas as pd
import numpy as np
from prophet import Prophet
import matplotlib.pyplot as plt

prophet_df_4 = clean_df[['ds','Cauliflower']].rename(columns={'Cauliflower': 'y'})

mask = prophet_df_4['y'] == 0
prophet_df_4['y'] = prophet_df_4['y'].replace(to_replace=0, value=np.nan).ffill()

train_4 = prophet_df_4[prophet_df_4['ds'] < '2022-01-01']
test_4 = prophet_df_4[(prophet_df_4['ds'] >= '2022-01-01') & (prophet_df_4['ds'] < '2023-01-01')]

model_4 = Prophet(
    yearly_seasonality=True,
    weekly_seasonality=False,
    daily_seasonality=False
)

model_4.fit(train_4)
future_4 = model_4.make_future_dataframe(periods=24, freq='ME')
forecast_4= model_4.predict(future_4)

fig1 = model_4.plot(forecast_4)
fig1.savefig("forecast_plot_4.png", dpi=300, bbox_inches="tight")
plt.close(fig1)
fig2 = model_4.plot_components(forecast_4)
fig2.savefig("components_plot_4.png", dpi=300, bbox_inches="tight")
plt.close(fig2)