from bs4 import BeautifulSoup
import urllib2

req = urllib2.Request("http://www.smalltime.com/Haiku?main=10", headers={'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1664.3 Safari/537.36', "Accept" : "text/html"})
contents = urllib2.urlopen(req).read()
 
soup = BeautifulSoup(contents, "html5lib")

for tag in soup.find_all('strong'):
	for element in tag.children:
		print element.string