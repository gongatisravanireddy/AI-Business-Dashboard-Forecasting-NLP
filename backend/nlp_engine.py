import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    score = analyzer.polarity_scores(text)["compound"]

    if score >= 0.05:
        return "Positive"
    elif score <= -0.05:
        return "Negative"
    else:
        return "Neutral"

def get_sentiment_counts(reviews_df):
    sentiments = reviews_df["review"].apply(analyze_sentiment)
    return sentiments.value_counts()