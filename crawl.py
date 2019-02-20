import sys
import json
import random
import optparse
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from urllib import urlopen
import re
import feedparser
import time
import lxml

websites = []


def scrape_npr(page_link):
    page_response  = requests.get(page_link)
    soup = BeautifulSoup(page_response.content, 'html.parser')

    articles = soup.findAll('h2',attrs={'class':'title'})

    for article in articles :
        websites.append(article.a['href'])
        

def scrape_huff(page_link):
    d = feedparser.parse(page_link)
    for e in d.entries:
        websites.append(e.link)

    huff_search = {
        #"trump": "https://search.huffingtonpost.com/search?utf8=%E2%9C%93&p=trump&fr=huffpost_desktop",
        #"bernie": "https://search.huffingtonpost.com/search?utf8=%E2%9C%93&p=bernie&fr=huffpost_desktop",
        #"senate": "https://search.huffingtonpost.com/search?utf8=%E2%9C%93&p=senate&fr=huffpost_desktop",
        #"supreme court": "https://search.huffingtonpost.com/search?utf8=%E2%9C%93&p=supreme+court&fr=huffpost_desktop",
        #"republican": "https://search.huffingtonpost.com/search?utf8=%E2%9C%93&p=republican&fr=huffpost_desktop",
        #"democratic" : "https://search.huffingtonpost.com/search?utf8=%E2%9C%93&p=democratic&fr=huffpost_desktop",
        #"clinton" : "https://search.huffingtonpost.com/search?utf8=%E2%9C%93&p=clinton&fr=huffpost_desktop",
        "election" : "https://search.huffingtonpost.com/search?utf8=%E2%9C%93&p=election&fr=huffpost_desktop"
    }
    #search words
    for key in huff_search :
        scrape_huff_search(huff_search[key])


def scrape_huff_search(page_link):
    page_response  = requests.get(page_link)
    soup = BeautifulSoup(page_response.content, 'html.parser')

    #first page
    articles = soup.findAll('h4',attrs={'class':'pb-10'})
    for article in articles :
        websites.append(article.a['href'])

    #more pages
    next_page = soup.findAll('a',attrs={'class':'next'})
    count = 0

    time.sleep(10)

    while len(next_page) > 0 :
        #gets next page link
        next_site = next_page[0]['href']
        next_page_response = requests.get(next_site)
        next_soup = BeautifulSoup(next_page_response.content, 'html.parser')
        more_articles = next_soup.findAll('h4',attrs={'class':'pb-10'})

        for article in more_articles:
            print(article.a['href'])
            websites.append(article.a['href'])
        
        next_page = next_soup.findAll('a',attrs={'class':'next'})
        count = count+1
        time.sleep(15)

    print(count)

def scrape_fox(page_link) :
    page_link = "https://www.foxnews.com/category/politics/elections"
    page_response  = requests.get(page_link)
    soup = BeautifulSoup(page_response.content, 'lxml')

    time.sleep(5)
    main_content = urljoin(page_link,soup.select(".load-more-data")[0]['data-ajaxurl'])
    main_response = requests.get(main_content)
    soup = BeautifulSoup(page_response.content, 'lxml')
    articles = main_response.select(".title")
    print(len(articles))

    #articles = soup.findAll('h4',attrs={'class':'title'})
    #for article in articles :
    #    link = article.a['href']
    #    if(link[0] == '/'):
    #        link = "https://www.foxnews.com" + link
    #        print(link)


def main() :
    news = {
        "npr":"https://www.npr.org/sections/politics/archive",
        "huff":"https://www.huffingtonpost.com/section/politics/feed",
        "fox": "https://www.foxnews.com/politics"
    }

    fox_news = {
        "trump" : "https://www.nbcnews.com/pages/search/?q=trump"
    }
    #scrape_npr(news["npr"])
    #scrape_huff(news["huff"])
    scrape_fox(fox_news["trump"])
    #print(len(websites))

    f = open("fox_trump", "a")
    for site in websites:
        f.write(site)
        f.write("\n")

if __name__ == "__main__":
    main()
