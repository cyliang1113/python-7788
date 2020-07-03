#爬虫
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

url = 'https://en.wikipedia.org/wiki/Kevin_Bacon'
conn = urlopen(url)
html = conn.read()
# print(html)

bs = BeautifulSoup(html, features="html.parser")
# for link in bs.findAll('a'):
#     if 'href' in link.attrs:
#         link_href = link.attrs['href']
#         if re.match('^(/wiki)', link_href):
#             print(link_href)

print(bs.h1.get_text())
print(bs.find(id='bodyContent').get_text())


