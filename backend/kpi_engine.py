import pandas as pd

def load_sales_data(path):
    df = pd.read_csv(path)
    df['order_date'] = pd.to_datetime(df['order_date'])
    return df

def calculate_kpis(df):
    total_revenue = df['sales'].sum()
    total_profit = df['profit'].sum()

    profit_margin = (total_profit / total_revenue) * 100

    # Month-over-Month Growth
    monthly_sales = df.resample('M', on='order_date')['sales'].sum()
    mom_growth = monthly_sales.pct_change().mean() * 100

    # Top product
    top_product = df.groupby('product')['sales'].sum().idxmax()

    # Top region
    top_region = df.groupby('region')['sales'].sum().idxmax()

    return {
        "total_revenue": round(total_revenue, 2),
        "total_profit": round(total_profit, 2),
        "profit_margin": round(profit_margin, 2),
        "mom_growth": round(mom_growth, 2),
        "top_product": top_product,
        "top_region": top_region
    }