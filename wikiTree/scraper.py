from bs4 import BeautifulSoup
import requests


class Scraper:
	def getLinks(url):
		soup = BeautifulSoup(requests.get(url).text, 'html.parser')
		links = soup.select('div#bodyContent a')
		result = {}
		for link in links:
			href = link.get('href')
			if not (link.string and href and href.startswith('/wiki/') and ':' not in href):
				continue
			title = link.string[:1].upper() + link.string[1:]
			result[title] = f'https://en.wikipedia.org{href}'
		return result

# result = getLinks("https://en.wikipedia.org/wiki/Computer_science")
# print(result)
