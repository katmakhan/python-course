#For invoking http requests
import requests

#Json Parsing
import json


def nifty_intradaychart():
	actualurl='https://groww.in/v1/api/charting_service/v2/chart/delayed/exchange/NSE/segment/CASH/NIFTY/daily?intervalInMinutes=1&minimal=true'
	res = requests.get(actualurl,timeout=2)
	fnolistdata=res.json()
	# print(fnolistdata)
	return fnolistdata


def nifty_topoptions():
	
	actualurl='https://groww.in/v1/api/stocks_fo_data/v1/contracts/nifty/top'
	res = requests.get(actualurl,timeout=2)
	fnolistdata=res.json()
	# print(fnolistdata)
	return fnolistdata
	
# def main():
# 	nifty_intradaychart()
	
# #Main program
# if __name__ == '__main__':
# 	main()