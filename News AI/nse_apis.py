#For invoking http requests
import requests

#Json Parsing
import json

from datetime import datetime

#Convert date object to date string
def convert_to_date_obj(date_str,date_format):
	date_obj = datetime. strptime(date_str,date_format)
	return date_obj

#Convert date string into date object
def convert_to_date_str(date_obj,date_format):
	date_str=date_obj.strftime(date_format)
	return date_str
	
def stock_opt():
	#Fetching NIFTY Stocks
	# actualurl='https://www.nseindia.com/api/liveEquity-derivatives?index=top20_contracts'
	# actualurl="https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY"
	# actualurl="https://www.nseindia.com/api/option-chain-equities?symbol=ABB"
	actualurl='https://www.nseindia.com/api/liveEquity-derivatives?index=stock_opt'

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

	fnolistdata=res.json()['data']
	# print(fnolistdata)

	s.close()
	return fnolistdata

def active_calls():
	#Fetching NIFTY Stocks
	# actualurl='https://www.nseindia.com/api/liveEquity-derivatives?index=top20_contracts'
	# actualurl="https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY"
	# actualurl="https://www.nseindia.com/api/option-chain-equities?symbol=ABB"
	actualurl='https://www.nseindia.com/api/snapshot-derivatives-equity?index=contracts&limit=20'

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

	fnolistdata=res.json()['volume']['data']
	# print(fnolistdata)

	s.close()
	return fnolistdata


def underlying_info():

	#Visit the main page to bypass cookies
	#Session to maintain the cookies
	s = requests.Session()

	# Headers for useragent
	headers = {
	"Accept-Encoding": "gzip, deflate, br",
	# "Accept-Language": "en-US,en;q=0.5",
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
	
	# To set the cookies, by visiting the mainpage
	mainurl = "https://www.nseindia.com/"
	response = s.get(mainurl,headers=headers,timeout=2)
	cookies = s.cookies
	# print(cookies)

	#Then visit the json page for fetching the json
	actualurl='https://www.nseindia.com/api/underlying-information'
	res = s.get(actualurl,headers=headers,timeout=2)
	# print(res.json())

	s.close()
	return res.json()

def marketstatus():

	#Visit the main page to bypass cookies
	#Session to maintain the cookies
	s = requests.Session()

	# Headers for useragent
	headers = {
	"Accept-Encoding": "gzip, deflate, br",
	# "Accept-Language": "en-US,en;q=0.5",
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
	
	# To set the cookies, by visiting the mainpage
	mainurl = "https://www.nseindia.com/"
	response = s.get(mainurl,headers=headers,timeout=2)
	cookies = s.cookies
	# print(cookies)

	#Then visit the json page for fetching the json
	actualurl='https://www.nseindia.com/api/marketStatus'
	res = s.get(actualurl,headers=headers,timeout=2)
	# print(res.json())

	s.close()
	return res.json()

def marketChart_indices(which):

	#Visit the main page to bypass cookies
	#Session to maintain the cookies
	s = requests.Session()

	# Headers for useragent
	headers = {
	"Accept-Encoding": "gzip, deflate, br",
	# "Accept-Language": "en-US,en;q=0.5",
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
	
	# To set the cookies, by visiting the mainpage
	mainurl = "https://www.nseindia.com/"
	response = s.get(mainurl,headers=headers,timeout=2)
	cookies = s.cookies
	# print(cookies)

	#Then visit the json page for fetching the json
	actualurl=f'https://www.nseindia.com/api/chart-databyindex?index={which}&indices=true'
	res = s.get(actualurl,headers=headers,timeout=2)
	# print(res.json())

	s.close()
	return res.json()
	

def index_optionchain(symbol):
	#Fetching NIFTY Stocks
	actualurl='https://www.nseindia.com/api/option-chain-indices?symbol='+symbol

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

	fnolistdata=res.json()['records']['data']
	# print(fnolistdata)

	s.close()
	return fnolistdata

def stock_optionchain(symbol):
	#Fetching NIFTY Stocks
	actualurl='https://www.nseindia.com/api/option-chain-equities?symbol='+symbol

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

	fnolistdata=res.json()['records']['data']
	# print(fnolistdata)

	s.close()
	return fnolistdata

def underlying_fnolist():
	#Fetching NIFTY Stocks
	actualurl='https://www.nseindia.com/api/underlying-information'

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

	fnolistdata=res.json()['data']['UnderlyingList']
	# print(fnolistdata)

	s.close()
	return fnolistdata


def fno_holiday_list():
	#Fetching NIFTY Stocks
	url='https://www.nseindia.com/api/holiday-master?type=trading'
	# https://www.nseindia.com/api/holiday-master?type=clearing
	
	headers = {
	#'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	#'Accept-Encoding': 'gzip, deflate, br',
	#'Accept-Language': 'en-US;q=0.5',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36'
	}
	
	#This website prevents normal Traffic, unlesss you specify the user agent, the server won't response
	resp = requests.get(url,headers=headers)
	# print("Done..")
	# print(resp)
	holidays = resp.json()	
	fno_holidays=holidays["FO"]
	# print(holidays)

	return fno_holidays

def index_expiry(index):
	url="https://www.nseindia.com/api/quote-derivative?symbol="+index
	headers = {
	#'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	#'Accept-Encoding': 'gzip, deflate, br',
	#'Accept-Language': 'en-US;q=0.5',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36'
	}
	
	#This website prevents normal Traffic, unlesss you specify the user agent, the server won't response
	resp = requests.get(url,headers=headers)
	# print("Done..")
	# print(resp)
	expirylist = resp.json()	
	explist=set(expirylist['expiryDates'])

	expirylistobj=[]
	for expdate_str in explist:
		expdate_obj=convert_to_date_obj(expdate_str,"%d-%b-%Y")
		print(expdate_str)
		expirylistobj.append(expdate_obj)

	expirylistobj.sort()
	latest_exp_obj=expirylistobj[0]
	print(latest_exp_obj)
	return latest_exp_obj

# index_expiry('NIFTY')
# index_expiry('BANKNIFTY')

def check_holiday(fno_holidays):
	#Check whether today is holiday or not
	currentday=datetime.now()

	holiday=False
	for holiday in fno_holidays:
		# FO - Futures and Options
		holiday_str=holiday["tradingDate"]
		# print(holiday_str)
		holidate_dateobj=convert_to_date_obj(holiday_str,"%d-%b-%Y")

		if holidate_dateobj.day==currentday.day:
			# print("Today is holiday")
			holiday=True
			break

			#To exit with false for combine scripting in CRON jobs
			# exit(1)
	if holiday==True:
		print("Today is holiday")
	else:
		print("Today is Not holiday")

	return holiday


def get_historical_data(stockname,from_date,to_date):
	actualurl=f'https://www.nseindia.com/api/historical/cm/equity?symbol={stockname}&series=[%22EQ%22]&from={from_date}&to={to_date}'
	headers = {
	#'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	"Accept-Encoding": "gzip, deflate, br",
	#'Accept-Language': 'en-US;q=0.5',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36'
	}


	#Visit the main page to bypass cookies
	s = requests.Session()

	# To set the cookies
	mainurl = "https://www.nseindia.com/"
	response = s.get(mainurl,headers=headers,timeout=2)

	print("checking url ",actualurl)
	#Then visit the json page for fetching the json
	resp = s.get(actualurl,headers=headers,timeout=2)
	
	print("Done..")
	# print(resp)
	historical_data = resp.json()	
	historical_data=historical_data["data"]
	s.close()
	return historical_data

def get_corporate_info(stockname):
	actualurl=f'https://www.nseindia.com/api/top-corp-info?symbol={stockname}&market=equities'
	headers = {
	#'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	"Accept-Encoding": "gzip, deflate, br",
	#'Accept-Language': 'en-US;q=0.5',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36'
	}


	#Visit the main page to bypass cookies
	s = requests.Session()

	# To set the cookies
	mainurl = "https://www.nseindia.com/"
	response = s.get(mainurl,headers=headers,timeout=2)

	print("checking url ",actualurl)
	#Then visit the json page for fetching the json
	resp = s.get(actualurl,headers=headers,timeout=2)
	
	print("Done..")
	# print(resp)
	data = resp.json()	
	# data=data["latest_announcements"]
	s.close()
	return data


def get_intraday_chart_data(stockname):
	actualurl=f'https://www.nseindia.com/api/chart-databyindex-dynamic?index={stockname}EQN&type=symbol'
	headers = {
	#'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	"Accept-Encoding": "gzip, deflate, br",
	#'Accept-Language': 'en-US;q=0.5',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36'
	}


	#Visit the main page to bypass cookies
	s = requests.Session()

	# To set the cookies
	mainurl = "https://www.nseindia.com/"
	response = s.get(mainurl,headers=headers,timeout=2)

	print("checking url ",actualurl)
	#Then visit the json page for fetching the json
	resp = s.get(actualurl,headers=headers,timeout=2)
	
	print("Done..")
	# print(resp)
	data = resp.json()	
	data=data["grapthData"]
	s.close()
	return data


# def main():
# 	fnolistdata=stock_opt()
# 	for data in fnolistdata:
# 		symbol=data['identifier']
# 		print(symbol)
	
# #Main program
# if __name__ == '__main__':
# 	main()