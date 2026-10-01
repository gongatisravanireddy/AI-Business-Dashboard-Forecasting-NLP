import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error

def forecast_sales(sales_df):
    # Convert to monthly sales
    monthly_sales = sales_df.resample('M', on='order_date')['sales'].sum()

    # Train test split
    train = monthly_sales[:-3]
    test = monthly_sales[-3:]

    # Train ARIMA
    model = ARIMA(train, order=(5, 1, 0))
    model_fit = model.fit()

    # Forecast next 3 months
    forecast = model_fit.forecast(steps=3)

    # Accuracy
    mae = mean_absolute_error(test, forecast)
    mape = mean_absolute_percentage_error(test, forecast) * 100

    forecast_values = forecast.tolist()

    return forecast_values, mae, mape