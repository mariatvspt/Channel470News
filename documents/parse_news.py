from newspaper import Article
import newspaper
import json
import os

urls = {'yahoo_trump': 'https://news.search.yahoo.com/search?p=trump&fr=uh3_news_vert_gs&fr2=p%3Anews%2Cm%3Asb'}

for name, url in urls.items():
    cnn_paper = newspaper.build(url, memoize_articles=False)
    all_articles = []
    i = cnn_paper.size()
    counter = 0

    for article in cnn_paper.articles :
        try:
            article.download()
            article.parse()
            an_article = {}
            
            a = Article(url)

            if(url.find("huff") > 0):
                an_article["source"] = "huffington"
            elif(url.find("cnn") > 0):
                an_article["source"] = "cnn"
            t = a.publish_date
            an_article["date"] = t.strftime('%m/%d/%Y')
            an_article["text"] = a.text
            all_articles.append(an_article)
            counter += 1
            print('Downloading [%d/%d]\r' % (counter,i), end="")
                
        except Exception as e:
            print(e)
            continue
            
    with open(name+ '.json', 'w') as outfile:
        json.dump(all_articles, outfile)

