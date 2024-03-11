from transformers import pipeline
import pandas as pd

# Initialize the Hugging Face sentiment analysis pipeline
nlp = pipeline('sentiment-analysis', model='distilbert-base-uncased__sst5__all-train')

with open("Cleaned Tesla Tweets.txt", 'r', encoding='utf-8') as f:
    tweets = f.readlines()

tweets = [tweet.strip() for tweet in tweets]

results = []

for tweet in tweets:
    result = nlp(tweet)[0]
    results.append((tweet, result['label']))

# Creating a dataframe to visualize the data better
df = pd.DataFrame(results, columns=["Tweets", "Sentiment"])

# Writing to a CSV file
df.to_csv('sentiment_analysis_bert.csv', index=False)
