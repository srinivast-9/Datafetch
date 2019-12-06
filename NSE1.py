from urllib.request import urlopen as uReq
from urllib.request import Request
#import urllib, json
import pandas_datareader as web
from bs4 import BeautifulSoup as soup
import json
import re
stock=input("Enter STOCK Name: ")

myUrl = "https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol="+stock+"&illiquid=0&smeFlag=0&itpFlag=0"
print("URL Generated: ", myUrl)

req = Request(
    myUrl, 
    data=None, 
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
    }
)

uClient = uReq(req)
pageHtml = uClient.read()
srch = '"lastPrice":"(.+?)"'

import urllib.request, json 
with urllib.request.urlopen("http://maps.googleapis.com/maps/api/geocode/json?address=google") as url:
    data = json.loads(url.read().decode())
    print(data) 

#response = urllib.urlopen(myUrl)
#data = json.loads(response.read())
#print(data)


#data = json.loads(uClient.read().decode())
#print(data)
#text = json.loads(str(pageHtml))


com = re.compile(srch)
rslt = re.findall(com, str(pageHtml))
srch1 = '"Symbol P/E: ""(.+?)"'
print(srch1)
#print(json.PE)
com1 = re.compile(srch1)
rslt1 = re.findall(com1, str(pageHtml))

print(rslt1)

if (rslt):
	print('Last Price of STOCK: ',stock, ' is ', str(rslt))

