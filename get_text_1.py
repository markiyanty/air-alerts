import os
import calendar
import re
import pandas
from nltk.corpus import stopwords


# remove all line without dot(first lines with authors names and date and also image signature)
# remove sentences with words Click and Note
def suitable_string(string):
    return len(string.strip()) != 0 and "Click" not in string \
           and "Note" not in string and "." in string and "W." not in string


def get_date(date):
    date = date.split("-")
    return " " + calendar.month_name[int(date[1])].capitalize() + " " + str(int(date[2]))


# remove mention repost date
def remove_date(data, date):
    return re.sub(get_date(date), "", data)


def clear_text(data):
    text = ""
    for line in data.split("\n"):
        if suitable_string(line):
            line = line.strip().lower()
            # remove punctuations
            line = line.translate(data.maketrans(' ', ' ', ',:!.();“”~@?\"[]*/_‘{}=$#%&"“”—'))

            line = line.replace("-", " ")
            # remove all digits
            line = re.sub(r"[\d]", "", line)

            # remove stopwords
            stopwords_ = stopwords.words("english")
            stopwords_.extend(["th", "st", "nd", "pm", "hours", "km", "m", "meters", "kilometers", "am", "e"])
            for word in line.split():
                if word not in stopwords_:
                    text += word + " "

            # remove copyright sign
            text = re.sub(r"©", "", text)

            # remove extra spaces
            text = text.replace("  ", " ")

    return text


def get_text_v1(csv_file):
    df = pandas.read_csv(csv_file)
    for i in range(len(df.index)):
        df.loc[i, ['text_v1']] = [remove_date(df.loc[i]['text_v0'], df.loc[i]['date'])]
    df['text_v1'] = df['text_v1'].apply(lambda x: clear_text(x))
    df.to_csv(csv_file, encoding="utf-8",index=False)
