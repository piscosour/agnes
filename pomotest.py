from bs4 import BeautifulSoup
import urllib2

req = urllib2.Request("http://www.elsewhere.org/pomo/", headers={"Accept" : "text/html"})
contents = urllib2.urlopen(req).read()
 
soup = BeautifulSoup(contents, "html5lib")

h3counter = 0

for div in soup.find_all('div', class_='storycontent'):
	for element in div.contents:
		if element.name == 'h1':
			print element.string
		elif element.name == 'h3' and h3counter < 1:
			print element.string
			h3counter = h3counter + 1
		elif element.name == 'h3' and h3counter == 1:
			break
		elif element.name == 'p' and element.string is not None:
			print element.string