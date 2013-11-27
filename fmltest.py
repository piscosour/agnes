from bs4 import BeautifulSoup
import urllib2

req = urllib2.Request("http://www.fmylife.com/random", headers={"Accept" : "text/html"})
contents = urllib2.urlopen(req).read()
 
soup = BeautifulSoup(contents, "html5lib")

h3counter = 0

for div in soup.find_all('div', class_='post article', limit=1):
	pre_text = ''.join(div.find_all(text=True))
	proc_text = pre_text.split('#')

	print proc_text[0]