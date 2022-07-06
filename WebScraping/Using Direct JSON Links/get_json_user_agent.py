#For invoking http requests
import requests

#Json Parsing
import json

	
def main():
	#Fetching NIFTY Stocks
	url='https://www1.nseindia.com/live_market/dynaContent/live_watch/stock_watch/niftyStockWatch.json'
	
	headers = {
	#'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	#'Accept-Encoding': 'gzip, deflate, br',
	#'Accept-Language': 'en-US;q=0.5',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36'
	}
	
	print("Fetching url...")
	
	#This website prevents normal Traffic, unlesss you specify the user agent, the server won't response
	resp = requests.get(url,headers=headers)
	print("Done..")
	print(resp)
	data = resp.json()	
	print(data)
	
#Main program
if __name__ == '__main__':
	main()