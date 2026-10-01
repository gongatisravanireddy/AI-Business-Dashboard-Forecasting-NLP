from backend.kpi_engine import load_sales_data, calculate_kpis

df = load_sales_data("data/sales_data.csv")
kpis = calculate_kpis(df)

print("Total Revenue:", kpis["total_revenue"])
print("Total Profit:", kpis["total_profit"])
print("Profit Margin:", kpis["profit_margin"], "%")
print("MoM Growth:", kpis["mom_growth"], "%")
print("Top Product:", kpis["top_product"])
print("Top Region:", kpis["top_region"])
