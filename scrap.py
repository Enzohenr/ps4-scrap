from urllib.request import urlopen

from urllib.error import HTTPError

from urllib.error import URLError

from bs4 import BeautifulSoup


try:

	html = urlopen("https://store.playstation.com/es-cl/home/games")

except HTTPError as e:
	print(e)

except URLError:

	print("Server down or incorrect domain")

else:

	res = BeautifulSoup(html.read(), "html5lib")

	linkOfSpan = []
	for li in res.findAll("div", class_="grid-cell__body"):
		print ((li.span).text)
		print ((li.h3).text)

