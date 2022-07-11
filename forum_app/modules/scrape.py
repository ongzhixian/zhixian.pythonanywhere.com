# The process of downloading data
# And then parsing it (RET) FET Fetext
# Fetch / Retrieve 
# Extract 
# Transform

# class FetchExtract(object):
#     def __init__(self):
#         pass

from forum_app import app_path
from os import path
from urllib import request

def get_airline(page_number=1):

    out_file_path = path.join(app_path, 'data', 'shared_data', f'airline-page{page_number}.html')

    target_url = f'https://www.iata.org/en/publications/directories/code-search/?airline.page={page_number}&airline.search='

    with request.urlopen(target_url) as response:
        html = response.read().decode('utf-8')
        with open(out_file_path, 'w', encoding='utf8') as outfile:
            outfile.write(html)
    