import pandas as pd
import numpy as np

products = ["Laptop", "Phone", "Tablet", "Headphones"]

positive_reviews = [
    "Excellent product quality",
    "Very fast delivery",
    "Amazing performance",
    "Worth the price",
    "Highly recommend this product"
]

negative_reviews = [
    "Very poor battery life",
    "Delivery was delayed",
    "Product stopped working",
    "Not worth the money",
    "Very bad customer support"
]

data = []

for _ in range(300):
    product = np.random.choice(products)

    if np.random.rand() > 0.5:
        review = np.random.choice(positive_reviews)
        rating = np.random.randint(4, 6)
    else:
        review = np.random.choice(negative_reviews)
        rating = np.random.randint(1, 3)

    data.append([review, product, rating])

df = pd.DataFrame(data, columns=["review", "product", "rating"])
df.to_csv("data/reviews_data.csv", index=False)

print("✅ reviews_data.csv created")