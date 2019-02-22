import newspaper
import json

urls = {'abc': 'https://abcnews.go.com/', 'huffington': 'https://www.huffingtonpost.com/'}

for name, url in urls.items():
	cnn_paper = newspaper.build(url, memoize_articles=False)

	all_articles = {}

	i = cnn_paper.size()
	counter = 0

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

