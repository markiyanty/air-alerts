from sklearn.feature_extraction.text import TfidfVectorizer
import os
import pandas
import json


def vectoraize_text(csv_file):
    df = pandas.read_csv("isw/isw.csv")
    # Initialize the TfidfVectorizer
    vectorizer = TfidfVectorizer()
    # Create an empty list to store the vectorized documents
    vectorized_docs = []
    for i in range(len(df.index)):
        vectorized_docs.append(df.loc[i]['stemm_text'])

    # Use the vectorizer to calculate the TF-IDF scores for each word
    tfidf_matrix = vectorizer.fit_transform(vectorized_docs)

    # Get the feature names (i.e., the words)
    feature_names = vectorizer.get_feature_names_out()

    for i in range(len(df.index)):
        scores = tfidf_matrix[i, :]
        dictionary = {}
        for j in range(len(feature_names)):
            score = scores[0, j]
            dictionary[feature_names[j]] = score
        df.loc[i, ['vector']] = json.dumps(dictionary)
    df.to_csv(csv_file, encoding="utf-8", index=False)
