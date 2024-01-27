#For invoking http requests
import requests

#Json Parsing
import json


def mostactive_calls():
	#Visit the main page to bypass cookies
	s = requests.Session()

	headers = {
	"Accept-Encoding": "gzip, deflate, br",
	"Accept-Language": "en-US,en;q=0.5",
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
	
	# To set the cookies
	mainurl = "https://trendlyne.com/futures-options/options/most-active-contract-call/"
	response = s.get(mainurl,headers=headers,timeout=2)

	#Then visit the json page for fetching the json
	#Fetching Active Calls
	actualurl='https://trendlyne.com/futures-options/api-filter/options/26-oct-2023-near/most_active_contract_call/all/'
	res = s.get(actualurl,headers=headers,timeout=2)
	fnolistdata=res.json()
	# print(fnolistdata)
	return fnolistdata

# def main():
# 	mostactive_calls()
	
# #Main program
# if __name__ == '__main__':
# 	main()