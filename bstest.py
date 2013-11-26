from bs4 import BeautifulSoup
import urllib2

req = urllib2.Request("http://www.fiftyshadesgenerator.com/", headers={"Accept" : "text/html"})
contents = urllib2.urlopen(req).read()
 
soup = BeautifulSoup(contents, "html5lib")
 
for para in soup.find_all('p'):
	try:
		if para['id'] == "text":
			print para.contents
			break
	except KeyError:
		pass
