from backend.nlp_engine import load_reviews, analyze_sentiment, extract_keywords

df = load_reviews("data/reviews_data.csv")

df, sentiment_counts = analyze_sentiment(df)

negative_keywords = extract_keywords(df, 'Negative')

print("Sentiment Counts:")
print(sentiment_counts)

print("\nTop Negative Keywords:")
print(negative_keywords)
