#For invoking http requests
import requests
from urllib.parse import urlencode, quote, unquote


#Json Parsing
import json


def getchart_indicators(emalabel,emavalue,query,use_live,limit,size,widget_id,end_time,timeframe,symbol,scan_link):

	#Session to maintain the cookies
	s = requests.Session()

	# Headers for content Type 
	headers = {
	"Accept": "application/json, text/plain, */*",
	"Content-Type": "application/x-www-form-urlencoded",
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
	

	testurl="https://chartink.com/"
	actualurl='https://chartink.com/stocks-new/process'
	res=s.get(testurl)
	# print(res)
	# print(res.cookies.get_dict())

	# Convert the xrf token
	encoded_xrf_token= unquote(res.cookies.get_dict()['XSRF-TOKEN'])
	headers["X-Xsrf-Token"]=encoded_xrf_token


	# Combine fields into a dictionary
	form_data = {
	    'query': query,
	    'use_live': use_live,
	    'limit': limit,
	    'size': size,
	    'widget_id': widget_id,
	    'end_time': end_time,
	    'timeframe': timeframe,
	    'symbol': symbol,
	    'scan_link': scan_link,
	}

	

	# print(headers)
	res = s.post(actualurl,headers=headers,data=form_data,timeout=3)
	# print(res)
	# print(res.json())

	s.close()
	return res.json()

# def main():
# 	# Separate fields
# 	emalabel = 'ema 20'
# 	emavalue='Ema(  Close , 20 )'
# 	use_live = "1"
# 	limit = "1"
# 	size = "200"
# 	widget_id = "-1"
# 	end_time = "-1"
# 	timeframe = "Daily"
# 	symbol = "HEROMOTOCO"
# 	scan_link = "null"
# 	query = f"select open, high, low, close, volume, {emavalue} as '{emalabel}' where symbol='{symbol}'"

# 	res=getchart_indicators(emalabel,emavalue,query,use_live,limit,size,widget_id,end_time,timeframe,symbol,scan_link)
	
# 	# Traverse the data
# 	groupdata=res.json()['groupData'][0]['results']
# 	for data in groupdata:
# 		# print(data)

# 		if data.get(emalabel) is not None:
# 			print(data[emalabel])
# 		print("---")

# #Main program
# if __name__ == '__main__':
# 	main()