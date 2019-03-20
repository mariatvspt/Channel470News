import newspaper
import json

urls = {'yahoo_trump': 'https://news.search.yahoo.com/search?p=trump&fr=uh3_news_vert_gs&fr2=p%3Anews%2Cm%3Asb'}
print('grace')

for name, url in urls.items():
	print('hi')
	cnn_paper = newspaper.build(url, memoize_articles=False)
	print('hi2')
	all_articles = {}
	print('hi3')
	i = cnn_paper.size()
	counter = 0

	print('Start')

	for article in cnn_paper.articles:
		try:
			article.download()
			article.parse()
			all_articles[article.url] = article.text
			counter += 1
			print('Downloading [%d/%d]\r' % (counter,i), end="")

		except Exception as e:
			print(e)
			continue

	with open(name+ '.json', 'w') as outfile:
		json.dump(all_articles, outfile)

