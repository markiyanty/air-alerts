import csv

import requests
import calendar
from datetime import timedelta, date
from bs4 import BeautifulSoup

URL_BASE = "https://understandingwar.org/backgrounder/"


# write line to the csv file
def write_to_csv(csv_file, link, date_):
    req = requests.get(link)
    if req.status_code == 200:
        with open(csv_file, "a",encoding="utf-8") as file:
            csv_writer = csv.writer(file)
            is_weekend = (date_.isoweekday() in [6, 7])
            bs = BeautifulSoup(req.text, "html.parser")
            title = bs.find_all("title")[0].text
            html = req.text
            csv_writer.writerow([str(date_), is_weekend, title, link, html])


def write_htmls(csv_file):
    # write first row to the csv file
    with open(csv_file, "w") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(["date", "isWeekend", "title", "url", "html"])

    # first day of starting collecting data
    start_date = date(2022, 2, 24)

    # adding not templated links
    not_templated_links = [URL_BASE + "russia-ukraine-warning-update-initial-russian-offensive-campaign-assessment",
                           URL_BASE + "russia-ukraine-warning-update-russian-offensive-campaign-assessment-february-25-2022",
                           URL_BASE + "russia-ukraine-warning-update-russian-offensive-campaign-assessment-february-26",
                           URL_BASE + "russia-ukraine-warning-update-russian-offensive-campaign-assessment-february-27",
                           URL_BASE + "russian-offensive-campaign-assessment-february-28-2022"]

    # write data from not templated links
    for link in not_templated_links:
        write_to_csv(csv_file, link, start_date)
        start_date += timedelta(1)

    # writing data from templated links
    while start_date != date(2023, 1, 26):
        link = f"{URL_BASE}russian-offensive-campaign-assessment-{calendar.month_name[start_date.month].lower()}-{start_date.day}"
        if start_date.year == 2023:
            link += f"-2023"
        write_to_csv(csv_file, link, start_date)
        start_date += timedelta(1)
