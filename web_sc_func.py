import urllib2
from bs4 import BeautifulSoup

def web_sc_func(url_path,return_data):
	url_path = raw_input("please enter url:")
	return_data = urllib2.urlopen(url_path)
	obj_parse = BeautifulSoup(return_data,'html.parser')
	return obj_parse
	