from bajra_model import model, test, forecast
from moong_model import model_2, test_2, forecast_2
from masur_model import model_3, test_3, forecast_3
from cauliflower_model import model_4, test_4, forecast_4
from sklearn.metrics import mean_absolute_percentage_error, root_mean_squared_error

# Bajra model
y_true = test['y'].values
y_pred = forecast.set_index('ds').loc[test['ds'], 'yhat'].values
mape = mean_absolute_percentage_error(y_true, y_pred)
print("MAPE:", mape)
rmse = root_mean_squared_error(y_true, y_pred)
print("RMSE:", rmse)

# Moong model
y_true = test_2['y'].values
y_pred = forecast.set_index('ds').loc[test_2['ds'], 'yhat'].values
mape = mean_absolute_percentage_error(y_true, y_pred)
print("MAPE:", mape)
rmse = root_mean_squared_error(y_true, y_pred)
print("RMSE:", rmse)

# Masur model
y_true = test_3['y'].values
y_pred = forecast.set_index('ds').loc[test_3['ds'], 'yhat'].values
mape = mean_absolute_percentage_error(y_true, y_pred)
print("MAPE:", mape)
rmse = root_mean_squared_error(y_true, y_pred)
print("RMSE:", rmse)

# Cauliflower model
y_true = test_4['y'].values
y_pred = forecast.set_index('ds').loc[test_4['ds'], 'yhat'].values
mape = mean_absolute_percentage_error(y_true, y_pred)
print("MAPE:", mape)
rmse = root_mean_squared_error(y_true, y_pred)
print("RMSE:", rmse)