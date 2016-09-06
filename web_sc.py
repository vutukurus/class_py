#web scrapping..
#Beautiful soup module
import urllib2
from bs4 import BeautifulSoup

url_path='http://www.bloomberg.com/quote/SPX:IND'

#Connect to the web..
return_data = urllib2.urlopen(url_path)

#Return data use bs4 to faciliate our usage..
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
obj_parse = BeautifulSoup(html_doc,'html.parser')
print obj_parse.title
print obj_parse.find_all('p') #all hits..
print obj_parse.find('p') #first hit..
print "=========="
print obj_parse.find(id="link2")

process_href= obj_parse.find_all('a')
for i in process_href:
	print i.get('class')










