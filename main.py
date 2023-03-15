from get_html import write_htmls
from get_text_0 import get_text
from get_text_1 import get_text_v1
from stemm_text import stemm_text
from lemm_text import lemm_text
from vectorize_text import vectoraize_text
import os


FOLDER_NAME = "isw/"
CSV_FILE_NAME = "isw.csv"
if __name__ == "__main__":
    # if folder doesn't exist
    if not os.path.exists(FOLDER_NAME):
        os.makedirs(FOLDER_NAME)

    csv_file_path = f"{FOLDER_NAME}{CSV_FILE_NAME}"
    
    write_htmls(csv_file_path)
    get_text(csv_file_path)
    get_text_v1(csv_file_path)
    stemm_text(csv_file_path)
    lemm_text(csv_file_path)
    vectoraize_text(csv_file_path)

