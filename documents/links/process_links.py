from newspaper import Article
import json
import os

def process_links(page_name):

	with open(page_name) as f:
	    content = f.readlines()

	all_articles = []

	counter = 0
	i = len(content)

	for url in content: 
		try:
			url = url.strip()
			a = Article(url)
			a.download()
			a.parse()
			an_article = {}
			an_article["source"] = "huffington"
			t = a.publish_date
			an_article["date"] = t.strftime('%m/%d/%Y')
			an_article["url"] = a.url
			an_article["text"] = a.text

			all_articles.append(an_article)

			counter += 1
			print('Downloading [%d/%d]\r' % (counter,i), end="")

		except Exception as e:
			print(e)
			continue

	filename = page_name + '.json'

	with open(filename, 'w') as outfile:
		json.dump(all_articles, outfile)

	print(len(all_articles))


process_links('huff_republican')