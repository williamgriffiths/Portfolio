from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


def load_tweets(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        tweets = file.readlines()
    return tweets


def remove_similar_tweets(tweets, threshold):
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(tweets)
    cosine_similarities = cosine_similarity(tfidf_matrix)

    duplicates = np.where(cosine_similarities > threshold)
    duplicate_indices = set()

    for i in range(len(duplicates[0])):
        if duplicates[0][i] != duplicates[1][i]:  # Excluding self comparison
            duplicate_indices.add(max(duplicates[0][i], duplicates[1][i]))  # Keeping the later tweet

    unique_tweets = [tweet for index, tweet in enumerate(tweets) if index not in duplicate_indices]
    return unique_tweets


def save_tweets(tweets, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(tweets)


if __name__ == "__main__":
    tweets = load_tweets("Tesla Tweets.txt")  # Load tweets
    unique_tweets = remove_similar_tweets(tweets, 0.8)  # Remove similar tweets
    save_tweets(unique_tweets, "unique_tweets.txt")  # Save unique tweets to a new file