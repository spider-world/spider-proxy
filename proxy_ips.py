# -*-coding:utf-8 -*-
import requests
import random
from bs4 import BeautifulSoup


def get_ip_list(ip_url, headers):
    web_data = requests.get(ip_url, headers=headers)
    html = web_data.text
    print(html)
    soup = BeautifulSoup(html, 'html')
    ips = soup.find_all('tr')
    ip_list = []
    for i in range(1, len(ips)):
        ip_info = ips[i]
        tds = ip_info.find_all('td')
        ip_list.append(tds[1].text + ':' + tds[2].text)
    for ip in ip_list:
        try:
            proxy_host = "https://" + ip
            proxy_temp = {"https": proxy_host}
            res = urllib.urlopen(url, proxies=proxy_temp).read()
        except Exception as e:
            ip_list.remove(ip)
            continue
    return ip_list


def get_random_ip(ip_list):
    proxy_list = []
    for ip in ip_list:
        proxy_list.append('http://' + ip)
    proxy_ip = random.choice(proxy_list)
    proxies = {'http': proxy_ip}
    return proxies


if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
    url = 'http://www.xicidaili.com/nn/'
    ip_list = get_ip_list(url, headers)
    proxies = get_random_ip(ip_list)
    print("代理ip为：")
    print(proxies)
