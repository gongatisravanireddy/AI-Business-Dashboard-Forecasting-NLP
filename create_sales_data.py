import pandas as pd
import numpy as np

np.random.seed(42)

dates = pd.date_range(start="2023-01-01", end="2024-12-31", freq="D")
products = ["Laptop", "Phone", "Tablet", "Headphones"]
regions = ["North", "South", "East", "West"]
segments = ["Consumer", "Corporate", "Home Office"]

data = []

for date in dates:
    for _ in range(np.random.randint(3, 8)):
        product = np.random.choice(products)
        region = np.random.choice(regions)
        segment = np.random.choice(segments)

        price = np.random.randint(500, 2000)
        quantity = np.random.randint(1, 5)

        sales = price * quantity
        profit = sales * np.random.uniform(0.1, 0.3)

        data.append([
            date, product, region, segment,
            price, quantity, sales, profit
        ])

df = pd.DataFrame(data, columns=[
    "order_date", "product", "region", "segment",
    "price", "quantity", "sales", "profit"
])

df.to_csv("data/sales_data.csv", index=False)

print("sales_data.csv created")
