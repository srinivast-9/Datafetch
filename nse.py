from bs4 import BeautifulSoup
import re
import urllib.request, json
from urllib.request import Request
stock=input("Enter STOCK Name: ")
url = "https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol="+stock+"&illiquid=0&smeFlag=0&itpFlag=0"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
response = urllib.request.urlopen(req).read()
soup = BeautifulSoup(response)
element = soup.body.find('P/E') 
print (element)