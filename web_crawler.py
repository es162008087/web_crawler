# web_crawler.py
# based on https://medium.com/@the.benhawy/how-i-made-a-python-web-crawler-to-automate-a-boring-daily-task-afb22fbffcc8

from urllib.request import urlopen
from bs4 import BeautifulSoup
import unicodedata
url = 'https://experto.dev/patron-de-diseno-strategy-en-java/'
page = urlopen(url)
soup = BeautifulSoup(page, 'html.parser')
