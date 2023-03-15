from nltk.stem import WordNetLemmatizer
import pandas


def lemmatizing(data):
    lemmatizer = WordNetLemmatizer()
    new_data = ""
    for word in data.split(" "):
        new_data += lemmatizer.lemmatize(word) + " "
    return new_data


def lemm_text(csv_file):
    df = pandas.read_csv(csv_file)
    df['lemm_text'] = df['text_v1'].apply(lambda x: lemmatizing(x))
    df.to_csv(csv_file, encoding="utf-8", index=False)
