from bajra_model import forecast, prophet_df
from moong_model import forecast_2, prophet_df_2
from masur_model import forecast_3, prophet_df_3
from cauliflower_model import forecast_4, prophet_df_4

last_date_1 = prophet_df['ds'].max()
last_date_2 = prophet_df_2['ds'].max()
last_date_3 = prophet_df_3['ds'].max()
last_date_4 = prophet_df_4['ds'].max()

future_forecast_1 = forecast[forecast['ds'] > last_date_1][
    ['ds', 'yhat', 'yhat_lower', 'yhat_upper']
]
future_forecast_2 = forecast_2[forecast_2['ds'] > last_date_2][
    ['ds', 'yhat', 'yhat_lower', 'yhat_upper']
]

future_forecast_3 = forecast_3[forecast_3['ds'] > last_date_3][
    ['ds', 'yhat', 'yhat_lower', 'yhat_upper']
]

future_forecast_4 = forecast_4[forecast_4['ds'] > last_date_4][
    ['ds', 'yhat', 'yhat_lower', 'yhat_upper']
]
print(future_forecast_1)
print(future_forecast_2)
print(future_forecast_3)
print(future_forecast_4)