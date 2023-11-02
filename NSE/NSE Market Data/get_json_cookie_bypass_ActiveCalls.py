#For invoking http requests
import requests

#Json Parsing
import json


def main():
	#Fetching NIFTY Stocks
	# actualurl='https://www.nseindia.com/api/liveEquity-derivatives?index=top20_contracts'
	# actualurl="https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY"
	# actualurl="https://www.nseindia.com/api/option-chain-equities?symbol=ABB"
	actualurl='https://www.nseindia.com/api/snapshot-derivatives-equity?index=contracts&limit=20'

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

	fnolistdata=res.json()['volume']['data']
	# print(fnolistdata)

	for data in fnolistdata:
		symbol=data['identifier']
		print(symbol)


	
#Main program
if __name__ == '__main__':
	main()