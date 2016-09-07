#Web Scrapping 
#Beautiful soup module 
#https://www.nseindia.com/

import urllib2
from bs4 import BeautifulSoup

url_path = "http://www.bseindia.com/"
return_data = urllib2.urlopen(url_path)

obj_parse = BeautifulSoup(return_data,'html.parser')
get_share_value = obj_parse.find('div',attrs={'class':'newsensexvalue'})

print "BSC SENSE Value:",get_share_value