import re

from bs4 import BeautifulSoup
import os
import pandas


def parse_text(html):
    bs = BeautifulSoup(html, "html.parser")
    main_div = bs.find_all("div", {"class": "field-type-text-with-summary"})[0]
    # deleting all tags
    main_div = re.sub(r"<(?:\"[^\"]*\"['\"]*|'[^']*'['\"]*|[^'\">])+>", "", main_div.text)
    # deleting all links
    main_div = re.sub(r"(https|http|ttp)(\S+.*\s)", "", main_div)
    # deleting all numbers like [12]
    main_div = re.sub(r"\[\d*\]", "", main_div)
    return main_div


def get_text(csv_file):
    df = pandas.read_csv(csv_file)
    df['text_v0'] = df['html'].apply(lambda x: parse_text(x))
    df.to_csv(csv_file, encoding="utf-8", index_label="id")
