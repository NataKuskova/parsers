from lxml import etree
from urllib.request import urlopen

r = urlopen('https://www.python.org/')
content = r.read()

root = etree.HTML(content)

# d = root.xpath('//div[@class="medium-widget blog-widget"]')
d = root.xpath('//div[contains(@class, "medium-widget blog-widget")]')
# print(d[0].text)
# print(d[0].attrib)

for i in range(0, len(d[0].xpath('.//ul//time'))):
    print(d[0].xpath('.//ul/li/time')[i].attrib['datetime'])
    print(d[0].xpath('.//ul/li/a/text()')[i])

# print(d[0].xpath('.//div/ul/li/time')[0].attrib['datetime'])
# print(d[0].xpath('.//div/ul/li/a/text()')[0])

