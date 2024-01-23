#For invoking http requests
import requests

#Json Parsing
import json


def stock_industry_data(symbol):

	# Headers for content Type 
	headers = {"Content-Type":"application/json"}


	data={}
	data['symbol']=symbol
	data=json.dumps(data)
	print(data)

	#Then visit the json page for fetching the json
	actualurl='https://webapi.niftytrader.in/webapi/Analysis/stock-industry-data'
	# https://webapi.niftytrader.in/webapi/Analysis/stock-financial-data
	
	res = requests.post(actualurl, data=data,headers=headers)
	print(res.json())
	return res.json()

def main():
	res=stock_industry_data("BPCL")

	if(res.get('resultData') is None):
		print("No result fetched")
		return

	#Quaterly Results
	lastThreeQTRModel=res['resultData']["lastThreeQTRModel"]

	for stocks in lastThreeQTRModel:
		print(stocks['sales_Revenue'])

#Main program
if __name__ == '__main__':
	main()