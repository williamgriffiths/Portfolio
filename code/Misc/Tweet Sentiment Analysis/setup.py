import nltk
from textblob import TextBlob
from nltk.corpus import stopwords
import pandas as pd


# Assuming tweets.txt is in the same directory as your python script
with open("Cleaned Tesla Tweets.txt", 'r', encoding='utf-8') as f:
    tweets = f.readlines()

# Removing any new line characters
tweets = [tweet.strip() for tweet in tweets]


def preprocess_data(text):
    text = text.lower()
    tokenized_text = nltk.word_tokenize(text)
    clean_text = [word for word in tokenized_text if word not in stopwords.words('english')]
    return " ".join(clean_text)

def get_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return 'Positive'
    elif analysis.sentiment.polarity == 0:
        return 'Neutral'
    else:
        return 'Negative'
    

processed_tweets = [preprocess_data(tweet) for tweet in tweets]
sentiments = [get_sentiment(tweet) for tweet in processed_tweets]


df = pd.DataFrame(list(zip(tweets, sentiments)), columns=["Tweets", "Sentiment"])
df_sorted = df.sort_values(by=['Sentiment'])
df_sorted.to_csv('Tesla Analysis.csv', index=False)
