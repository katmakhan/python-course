#import the modules
import requests
import traceback
import json

import helper_functions as help_functions

def getstockdetails(which):
	#Fetching NIFTY Stocks
	actualurl='https://www.nseindia.com/api/equity-stockIndices?index='+which

	#Visit the main page to bypass cookies
	s = requests.Session()


	headers = {
	"Accept-Encoding": "gzip, deflate, br",
	# "Accept-Language": "en-US,en;q=0.5",
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
	

	# To set the cookies
	mainurl = "https://www.nseindia.com/"
	response = s.get(mainurl,headers=headers,timeout=2)

	#Then visit the json page for fetching the json
	res = s.get(actualurl,headers=headers,timeout=2)
	# print(res.json())

	result=res.json()['data']
	# print(fnolistdata)

	s.close()
	return result

def main():
	nifty50stocks_json={}
	nifty50stocks=getstockdetails("NIFTY%2050")
	for stock in nifty50stocks:
		print(stock['symbol'])
		if stock['symbol'] != "NIFTY 50":
			nifty50stocks_json["NSE:"+stock['symbol']+"-EQ"]=100

	nifty200stocks_json={}
	nifty200stocks=getstockdetails("NIFTY%20200")
	skip=True
	for stock in nifty200stocks:
		print(stock['symbol'])
		if stock['symbol'] != "NIFTY 200":
			nifty200stocks_json["NSE:"+stock['symbol']+"-EQ"]=100

	# Sort them
	sorted_data_nifty50 = {k: nifty50stocks_json[k] for k in sorted(nifty50stocks_json)}
	sorted_data_nifty200 = {k: nifty200stocks_json[k] for k in sorted(nifty200stocks_json)}
	
	help_functions.writejson("./Data/NIFTY50_Stocks.json",sorted_data_nifty50)
	help_functions.writejson("./Data/NIFTY200_Stocks.json",sorted_data_nifty200)
	print("Done")
	
main()

# #Main program
# if __name__ == '__main__':
# 	try:
# 		main()

# 	except Exception as e:
# 		print("Reached here..")
# 		traceback.print_exc()
# 		print(e)

# 	finally:
# 		# update_telegram("Closed the Live Script","Restart the server")
# 		traceback.print_exc()
# 		print("Error ayi ..")