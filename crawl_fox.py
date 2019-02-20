from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
import time
import sys
import json
import random
import optparse
import requests
from bs4 import BeautifulSoup
from urllib import urlopen
import re
import feedparser
import time
import lxml

f = open("fox_election", "a")

driver_path = 'C:/chromedriver/chromedriver.exe'

driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.foxnews.com/category/politics/elections')
html = driver.page_source.encode('utf-8')

page_num = 0

for i in range(1,251):
    try:
        load_button = driver.find_element_by_css_selector('.button.load-more.js-load-more') 
    except StaleElementReferenceException as e:
        break
    load_button.click()
    page_num += 1
    print("getting page number "+str(page_num))
    time.sleep(1)

html = driver.page_source.encode('utf-8')

soup = BeautifulSoup(html, 'lxml')
articles = soup.find_all('h4', attrs={"class":'title'})
count = 0

for article in articles:
    link = article.a['href']
    if(link[0] == '/'):
        link = "https://www.foxnews.com" + link
        print(link)
        time.sleep(1)
        f.write(link)
        f.write("\n")

print(len(articles))

