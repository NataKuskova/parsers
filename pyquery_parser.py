import requests
from pyquery import PyQuery as pq
from time import sleep
from lxml import html


BASE_URL = 'http://hotline.ua'

"""
class Proxy:
    proxy_url = 'http://www.ip-adress.com/proxy_list/'
    proxy_list = []

    def __init__(self):
        r = requests.get(self.proxy_url)
        # str_ = pq(r.content)
        # result = str_('tr.odd td:first-child').text()
        str_ = html.fromstring(r.content)
        result = str_.xpath("//tr[@class='odd']/td[1]/text()")
        self.proxy_list = result

    def get_proxy(self):
        for proxy_ in self.proxy_list:
            url_ = 'http://' + proxy_
            try:
                r = requests.get('http://ya.ru', proxies={'http': url_})
                if r.status_code == 200:
                    return url_
            except requests.exceptions.ConnectionError:
                continue
"""


def parse_product(prod):
    characteristics_list = {}
    product_name = prod('.title-24.p_b-5').text()
    product_price = prod('.range-price.orng.g_statistic').text()
    description = prod('.full-desc.text-14').text()
    characteristics = prod('#full-props-list tr')
    for c in characteristics:
        characteristics_list[pq(c)('th span').text()] = pq(c)('td').text()
    print(number)
    print(product_name)
    print(product_price)
    print(description)
    print(characteristics_list)
    with open('products.txt', 'a+', encoding='utf-8') as f:
        f.write(str(number) + '\n')
        f.write(product_name + '\n')
        f.write(product_price + '\n')
        f.write(description + '\n')
        f.write(characteristics_list)
        f.write('\n\n')

if __name__ == '__main__':

    # proxy = Proxy()
    # proxy = proxy.get_proxy()
    # print(proxy)

    response = requests.get(BASE_URL + '/foto/fotoapparaty/')
    if response.status_code == 200:

        products = pq(response.content)
        num_pages = int(products('.cell.pager.p_t-10.p_b-20 span a:last-child').text())

        number = 1
        for i in products('.cell.gd-item.flex-block.flex-stretch.flex-wrap'):

            href = pq(i)('.m_r-10 a').attr['href']
            print(BASE_URL + href)
            resp = requests.get(BASE_URL + href)
            if resp.status_code == 200:
                product = pq(resp.content)
                parse_product(product)

                number += 1
            else:
                print('Server error.')
            sleep(3)

        if num_pages > 1:
            p_url = BASE_URL + '/foto/fotoapparaty/?p=%s'
            for url in [p_url % i for i in range(1, num_pages + 1)]:
                print(url)
                # response2 = requests.get(url, proxies={'http': proxy})
                response2 = requests.get(url)
                if response2.status_code == 200:
                    products_pages = pq(response2.content)

                    for i in products_pages('.cell.gd-item.flex-block.flex-stretch.flex-wrap'):
                        href = pq(i)('.m_r-10 a').attr['href']
                        print(BASE_URL + href)
                        resp = requests.get(BASE_URL + href)
                        if resp.status_code == 200:
                            product = pq(resp.content)
                            parse_product(product)
                            number += 1
                        else:
                            print('Server error.')
                        sleep(3)
                else:
                    print('Server error.')
                sleep(5)
    else:
        print('Server error.')
