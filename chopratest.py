from bs4 import BeautifulSoup
import urllib2

req = urllib2.Request("http://www.wisdomofchopra.com/iframe.php", headers={"Accept" : "text/html"})
contents = urllib2.urlopen(req).read()
 
soup = BeautifulSoup(contents, "html5lib")

h3counter = 0

for div in soup.find_all(id='quote'):
	print div.string