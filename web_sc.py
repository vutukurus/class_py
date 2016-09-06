#web scrapping..
#Beautiful soup module
import urllib2
from bs4 import BeautifulSoup

url_path='http://www.bloomberg.com/quote/SPX:IND'

#Connect to the web..
return_data = urllib2.urlopen(url_path)

#Return data use bs4 to faciliate our usage..
obj_parse = BeautifulSoup(return_data,'html.parser')
get_share_value=obj_parse.find('div',attrs={'class':'price'})
print get_share_value
print get_share_value.text

get_index_value = obj_parse.find('h1',attrs={'class':'name'})
print get_index_value
print get_index_value.text
