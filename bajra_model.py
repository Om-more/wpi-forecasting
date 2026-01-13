from data_filter import clean_df
import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt

prophet_df = clean_df[['ds','Bajra']].rename(columns={'Bajra': 'y'})
train = prophet_df[prophet_df['ds'] < '2022-01-01']
test  = prophet_df[(prophet_df['ds'] >= '2022-01-01') & (prophet_df['ds'] < '2023-01-01')]
model = Prophet(
    yearly_seasonality=True,
    weekly_seasonality=False,
    daily_seasonality=False
)

model.fit(train)
future = model.make_future_dataframe(periods=12, freq='ME')
forecast= model.predict(future)

fig1 = model.plot(forecast)
fig1.savefig("forecast_plot.png", dpi=300, bbox_inches="tight")
plt.close(fig1)
fig2 = model.plot_components(forecast)
fig2.savefig("components_plot.png", dpi=300, bbox_inches="tight")
plt.close(fig2)