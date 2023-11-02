#For invoking http requests
import requests

#Json Parsing
import json


def main():
	#Fetching NIFTY Stocks
	actualurl='https://www.nseindia.com/api/underlying-information'

	#Visit the main page to bypass cookies
	s = requests.Session()


	headers = {
	"Accept-Encoding": "gzip, deflate, br",
	"Accept-Language": "en-US,en;q=0.5",
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
	

	# To set the cookies
	mainurl = "https://www.nseindia.com/"
	response = s.get(mainurl,headers=headers,timeout=2)

	#Then visit the json page for fetching the json
	res = s.get(actualurl,headers=headers,timeout=2)
	print(res.json())

	fnolistdata=res.json()['data']['UnderlyingList']
	# print(fnolistdata)

	symbolist=[]
	for data in fnolistdata:
		symbol=data['symbol']
		print(symbol)
		symbolist.append(symbol)

	print(symbolist)

	
#Main program
if __name__ == '__main__':
	main()