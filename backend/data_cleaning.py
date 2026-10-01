import pandas as pd

def clean_sales_data(df):
    # Remove duplicates
    df = df.drop_duplicates()

    # Handle missing values
    df = df.dropna()

    # Convert data types
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['sales'] = pd.to_numeric(df['sales'], errors='coerce')
    df['profit'] = pd.to_numeric(df['profit'], errors='coerce')

    # Remove invalid rows (negative values)
    df = df[(df['sales'] >= 0) & (df['profit'] >= 0)]

    # Simple outlier removal (very high sales)
    upper_limit = df['sales'].quantile(0.99)
    df = df[df['sales'] <= upper_limit]

    return df

def clean_reviews_data(df):
    df = df.drop_duplicates()
    df = df.dropna()

    # Remove very short reviews
    df = df[df['review'].str.len() > 5]

    return df