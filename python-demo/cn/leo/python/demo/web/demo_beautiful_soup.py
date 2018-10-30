from urllib.request import urlopen
from bs4 import BeautifulSoup


url = 'http://www.baidu.com/'
conn = urlopen(url)
print(conn.info())
html = conn.read()
print(html)
bf = BeautifulSoup(html, features='html.parser')

print(bf.html.head.title)

mnav_l = bf.find_all('a', {'class' : 'mnav'})
for i in mnav_l:
    print(i)
    print(i.get_text())

print(bf.find(id='u'))
