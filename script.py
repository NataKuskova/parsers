from bs4 import BeautifulSoup
from urllib.request import urlopen

r = urlopen('https://www.python.org/')
content = r.read()

bs = BeautifulSoup(content, 'html.parser')
# print(bs.p.text)
# print(bs.a)
# print(bs.a['href'])
# print(bs.find_all('a'))
print(bs.find('div', {'class': 'row'}).prettify())
