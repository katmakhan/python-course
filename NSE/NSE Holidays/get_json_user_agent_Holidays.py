#For invoking http requests
import requests

#Json Parsing
import json

#Date Import
from datetime import datetime


#Convert date object to date string
def convert_to_date_obj(date_str,date_format):
	date_obj = datetime. strptime(date_str,date_format)
	return date_obj

#Convert date string into date object
def convert_to_date_str(date_obj,date_format):
	date_str=date_obj.strftime(date_format)
	return date_str

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
	
	print("Fetching url...")
	
	#This website prevents normal Traffic, unlesss you specify the user agent, the server won't response
	resp = requests.get(url,headers=headers)
	print("Done..")
	# print(resp)
	holidays = resp.json()	
	fno_holidays=holidays["FO"]
	# print(holidays)

	return fno_holidays

def check_holiday(fno_holidays):
	#Check whether today is holiday or not
	currentday=datetime.now()

	holiday=False
	for holiday in fno_holidays:
		# FO - Futures and Options
		holiday_str=holiday["tradingDate"]
		print(holiday_str)
		holidate_dateobj=convert_to_date_obj(holiday_str,"%d-%b-%Y")

		if holidate_dateobj.day==currentday.day:
			print("Today is holiday")
			holiday=True
			break

			#To exit with false for combine scripting in CRON jobs
			# exit(1)
	if holiday==True:
		print("Today is holiday")
	else:
		print("Today is Not holiday")

	return holiday

def main():
	fno_holidays=fno_holiday_list()
	check_holiday(fno_holidays)

#Main program
if __name__ == '__main__':
	main()