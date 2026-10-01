def generate_insights(kpis, forecast_values, sentiment_counts):
    insights = []

    # KPI insights
    insights.append(
        f"Total revenue is {kpis['total_revenue']:.2f} with a profit margin of {kpis['profit_margin']:.2f}%."
    )

    if kpis["mom_growth"] < 0:
        insights.append(
            f"Business shows a decline of {kpis['mom_growth']:.2f}% month-over-month."
        )
    else:
        insights.append(
            f"Business is growing at {kpis['mom_growth']:.2f}% month-over-month."
        )

    insights.append(
        f"Top performing product is {kpis['top_product']} and highest sales region is {kpis['top_region']}."
    )

    # Forecast insight
    avg_forecast = sum(forecast_values) / len(forecast_values)
    insights.append(
        f"Average forecasted monthly revenue for next period is {avg_forecast:.2f}."
    )

    # Sentiment insight
    if sentiment_counts.get("Positive", 0) > sentiment_counts.get("Negative", 0):
        insights.append("Customer sentiment is mostly positive.")
    else:
        insights.append("Customer sentiment needs attention due to higher negative feedback.")

    return insights