#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup


url = 'https://jerseyctf.xyz/'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

with open('dir','r') as directory:
    for d in directory:
        target = url + d
        response = requests.get(target, headers=headers)
        soup = BeautifulSoup(response.text,'html.parser')
        print(soup)
