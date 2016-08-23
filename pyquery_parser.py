from pyquery import PyQuery as pq
from urllib.request import urlopen


r = urlopen('https://hotline.ua/bt/holodilniki/')
content = r.read()

d = pq(content)

# print(d('div'))
# print(d('.medium-widget.blog-widget ul li'))
for i in d('.medium-widget.blog-widget ul li'):
    print(pq(i)('time').attr['datetime'])
    print(pq(i)('a').text())
