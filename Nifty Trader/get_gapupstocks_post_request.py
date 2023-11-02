#For invoking http requests
import requests

#Json Parsing
import json


from datetime import datetime
from datetime import timedelta

#Convert date object to date string
def convert_to_date_obj(date_str,date_format):
	date_obj = datetime. strptime(date_str,date_format)
	return date_obj

#Convert date string into date object
def convert_to_date_str(date_obj,date_format):
	date_str=date_obj.strftime(date_format)
	return date_str

def main():

	# Headers for content Type 
	headers = {"Content-Type":"application/json"}

	curr_day=datetime.today() - timedelta(days=0)
	curr_day_str=convert_to_date_str(curr_day,"%Y-%m-%d")

	data={}
	data['Date']=curr_day_str
	data=json.dumps(data)
	print(data)

	#Then visit the json page for fetching the json
	actualurl='https://webapi.niftytrader.in/webapi/Resource/gap-analysis'
	res = requests.post(actualurl, data=data,headers=headers)
	print(res.json())

	if(res.json().get('resultData') is None):
		print("No result fetched")
		return

	#Print gap-up stocks
	gap_up_stocks=res.json()['resultData']["gap_up_stocks"]
	gap_down_stocks=res.json()['resultData']["gap_down_stocks"]


	for stocks in gap_up_stocks:
		print(stocks['symbol_name'])

	
#Main program
if __name__ == '__main__':
	main()