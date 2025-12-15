import requests
import re
from bs4 import BeautifulSoup


url= 'http://localhost:8000/'
response= requests.get(url)

raw_html =response.text
parced_html= BeautifulSoup(raw_html, 'html.parser')

# print(parced_html.title)

top3_jobs_heading= parced_html.select_one('#intro > div > div > article > h2')

if top3_jobs_heading is not None:
    article= top3_jobs_heading.parent

    if article is not None:
        for p in article.select('p'):
            print(re.sub(r'\s{1,}', ' ', p.text).strip())
            print()
