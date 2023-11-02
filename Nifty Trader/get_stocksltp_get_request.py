#For invoking http requests
import requests

#Json Parsing
import json


def main():

	# Headers for content Type 
	headers = {"Content-Type":"application/json"}

	symbol="bpcl"

	#Then visit the json page for fetching the json
	actualurl='https://webapi.niftytrader.in/webapi/Symbol/symbol-ltp-chart?symbol='+symbol
	# https://webapi.niftytrader.in/webapi/Analysis/stock-financial-data
	
	res = requests.get(actualurl,headers=headers)
	print(res.json())

	if(res.json().get('resultData') is None):
		print("No result fetched")
		return

	chartdata=res.json()['resultData'][0]['chart_data']
	print(chartdata)

#Main program
if __name__ == '__main__':
	main()