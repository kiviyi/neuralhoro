import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import asyncio
import aiohttp
import nest_asyncio
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from loguru import logger
from datetime import datetime
import glob
from matplotlib import pyplot as plt
from collections import Counter
import time
from fake_useragent import UserAgent
from collections import Counter
import urllib
import csv
nest_asyncio.apply()



signs = ['aries', 'gemini', 'taurus', 'cancer', 'leo', 'virgo', 'libra', 'scorpio', 'sagittarius', 'capricorn',
         'aquarius', 'pisces']
data = pd.read_csv('data.csv', names=['date', 'sign', 'text'])


for i in range(2004, 2022):
    for j in range(1, 13):
        for k in range(1, 32):
            for sign in signs:
                try:
                    year = i
                    month = j
                    day = k
                    if month < 10:
                        month = '0' + str(month)
                    if day < 10:
                        day = '0' + str(day)
                    date = '%s-%s-%s' % (year, month, day)
                    url = 'https://horoscopes.rambler.ru/%s/%s/?updated' % (sign, date)  # url для второй страницы
                    print(url)
                    r = requests.get(url)
                    response = r.text.encode('utf-8')
                    soup = BeautifulSoup(response, features="lxml")
                    text = soup.find('p', class_='mtZOt').text
                    data = pd.concat([data, pd.DataFrame.from_records([{'date': date, 'sign': sign, 'text': text}])], ignore_index=True)
                    data.to_csv('data.csv', encoding='utf-8')
                    print('saved date=', date, ' sign= ', sign)
                except Exception:
                    continue