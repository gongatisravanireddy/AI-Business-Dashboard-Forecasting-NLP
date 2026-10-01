from flask import Flask, render_template, request
import pandas as pd

# Backend modules
from backend.data_cleaning import clean_sales_data, clean_reviews_data
from backend.kpi_engine import calculate_kpis
from backend.forecasting_engine import forecast_sales
from backend.nlp_engine import analyze_sentiment, get_sentiment_counts
from backend.insight_generator import generate_insights

app = Flask(__name__)

# -----------------------------
# LOAD AND CLEAN DATA (run once)
# -----------------------------
sales_df = pd.read_csv("data/sales_data.csv")
reviews_df = pd.read_csv("data/reviews_data.csv")

sales_df = clean_sales_data(sales_df)
reviews_df = clean_reviews_data(reviews_df)

# -----------------------------
# KPI CALCULATION
# -----------------------------
kpis = calculate_kpis(sales_df)

# -----------------------------
# FORECASTING
# -----------------------------
forecast_values, mae, mape = forecast_sales(sales_df)

# -----------------------------
# SENTIMENT ANALYSIS (DATASET)
# -----------------------------
sentiment_counts = get_sentiment_counts(reviews_df)

# -----------------------------
# AI INSIGHTS
# -----------------------------
insights = generate_insights(kpis, forecast_values, sentiment_counts)

# =============================
# HOME ROUTE
# =============================
@app.route("/")
def home():
    return render_template(
        "dashboard.html",
        kpis=kpis,
        forecast=forecast_values,
        sentiment=sentiment_counts.to_dict(),
        insights=insights,
        mae=round(mae, 2),
        mape=round(mape, 2),
        prediction=None
    )

# =============================
# REAL-TIME SENTIMENT ROUTE
# =============================
@app.route("/predict_sentiment", methods=["POST"])
def predict_sentiment():
    review_text = request.form["review_text"]
    sentiment = analyze_sentiment(review_text)

    return render_template(
        "dashboard.html",
        kpis=kpis,
        forecast=forecast_values,
        sentiment=sentiment_counts.to_dict(),
        insights=insights,
        mae=round(mae, 2),
        mape=round(mape, 2),
        prediction=sentiment
    )

# =============================
# RUN APP
# =============================
if __name__ == "__main__":
    app.run(debug=True, port=5001)
