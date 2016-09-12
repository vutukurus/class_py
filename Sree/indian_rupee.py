import urllib2
from bs4 import BeautifulSoup

url_path = 'http://www.xe.com/currency/inr-indian-rupee'

return_data = urllib2.urlopen(url_path)

obj_parse = BeautifulSoup(return_data,'html.parser')
#get_rupee_value = obj_parse.find('table id',attr={'class':'summary'})
#get_rupee_value = obj_parse.find('table id',attr={'class':'rateCell'})
get_rupee_value = obj_parse.find('a href="/currencycharts/?from=USD&to=INR"')
get_rupee_value = obj_parse.find("a")

print get_rupee_value

url_path1 = 'http://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To=INR'
return_data1 = urllib2.urlopen(url_path1)

obj_parse1 = BeautifulSoup(return_data1,'html.parser')

get_rupee_value1 = obj_parse1.find('td')

print get_rupee_value1
