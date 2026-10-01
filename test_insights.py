from backend.kpi_engine import load_sales_data, calculate_kpis
from backend.forecasting_engine import prepare_monthly_sales, train_test_split, train_arima, evaluate_model
from backend.nlp_engine import load_reviews, analyze_sentiment, extract_keywords
from backend.insight_generator import generate_insights

# Load data
sales_df = load_sales_data("data/sales_data.csv")
reviews_df = load_reviews("data/reviews_data.csv")

# KPIs
kpis = calculate_kpis(sales_df)

# Forecast
monthly_sales = prepare_monthly_sales(sales_df)
train, test = train_test_split(monthly_sales)
model = train_arima(train)
forecast, mae, mape = evaluate_model(model, train, test)

forecast_values = forecast.tolist()

# NLP
reviews_df, sentiment_counts = analyze_sentiment(reviews_df)
negative_keywords = extract_keywords(reviews_df, 'Negative')

# Insights
insights = generate_insights(kpis, forecast_values, sentiment_counts, negative_keywords)

print("AI Business Insights:\n")
for insight in insights:
    print("-", insight)
