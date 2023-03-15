from nltk.stem import PorterStemmer
import pandas


def stemming(data):
    stemmer = PorterStemmer()
    new_data = ""
    for word in data.split(" "):
        new_data += stemmer.stem(word) + " "
    return new_data


def stemm_text(csv_file):
    df = pandas.read_csv(csv_file)
    df['stemm_text'] = df['text_v1'].apply(lambda x: stemming(x))
    df.to_csv(csv_file, encoding="utf-8", index=False)
