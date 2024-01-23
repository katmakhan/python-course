#For invoking http requests
import requests

#Json Parsing
import json

#Time
import time

def stock_return(stockname):

	#Then visit the json page for fetching the json
	# stockname="ADANIPORTS"
	actualurl=f'https://portal.tradebrains.in/api/stock-returns/{stockname}/'
	print(actualurl)
	res = requests.get(actualurl)
	print(res.json())
	return res.json()

def stock_data(stockname):

	#Then visit the json page for fetching the json
	# stockname="ADANIPORTS"
	actualurl=f'https://portal.tradebrains.in/api/stock/{stockname}/prices?days=1&type=INTRADAY'
	print(actualurl)
	res = requests.get(actualurl)
	print(res.json())
	return res.json()


def screener_data():
	headers={
	"Accept":"application/json, text/plain, */*",
	"Content-Type": "application/json",
	"User-Agent" :"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
	}

	payload={"allFilters":[{"values":[0,2500000],"particular":"MCAP","operator":"&"}],"selectedColumns":["MCAP","PRICE","returns_1y","TTMPE","YIELD"],"offset":0,"sortBy":"MCAP","sortOrder":"DESC","industries":[],"indices":[]}
	actualurl='https://portal.tradebrains.in/api/screener/?page=1&per_page=25'
	print(actualurl)
	res = requests.post(actualurl,data=payload,headers=headers)
	print(res)
	print(res.json())
	return res.json()


def main():
	# stock_data("ADANIPORTS")

	# # print("Wait 5 seconds to not get server error")
	# # time.sleep(5)

	# stock_return("ADANIPORTS")

	# print("Wait 5 seconds to not get server error")
	# time.sleep(5)

	screener_data()

#Main program
if __name__ == '__main__':
	main()