from backend.kpi_engine import load_sales_data
from backend.forecasting_engine import (
    prepare_monthly_sales,
    train_test_split,
    train_arima,
    evaluate_model
)

df = load_sales_data("data/sales_data.csv")

monthly_sales = prepare_monthly_sales(df)

train, test = train_test_split(monthly_sales)

model = train_arima(train)

forecast, mae, mape = evaluate_model(model, train, test)

print("Forecast values:")
print(forecast)

print("\nMAE:", mae)
print("MAPE:", mape, "%")
