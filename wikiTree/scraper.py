from bs4 import BeautifulSoup
import requests
import random

class Scraper:
	# this function expects a wikipedia url and returns a dictionary with the titles of all the content links and the links to other wikipedia pages in the url passed in.
	@staticmethod
	def getLinks (url, linksSeen, maxNumOfLinks=8):
		soup = BeautifulSoup(requests.get(url).text, 'html.parser')
		links = soup.select('div#bodyContent a')
		result = {}
		for link in links:
			href = link.get('href')
			if not (link.string and href and href.startswith('/wiki/') and ':' not in href):
				continue
			title = link.string[:1].upper() + link.string[1:]
			if title in linksSeen:
				continue
			linksSeen.add(title)
			result[title] = f'https://en.wikipedia.org{href}'
		randomLinks = {}
		for _ in range(min(maxNumOfLinks,len(result))):
			k,v = random.choice(list(result.items()))
			randomLinks[k] = v
		return randomLinks


