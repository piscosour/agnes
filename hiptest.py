from bs4 import BeautifulSoup
import urllib2

req = urllib2.Request("http://hipsteripsum.me/?paras=1&type=hipster-centric", headers={'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1664.3 Safari/537.36', "Accept" : "text/html"})
contents = urllib2.urlopen(req).read()
 
soup = BeautifulSoup(contents, "html5lib")

for div in soup.find_all(id='content'):
	print div.contents[1].string