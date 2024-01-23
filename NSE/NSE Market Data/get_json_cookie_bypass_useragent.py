#For invoking http requests
import requests

#Json Parsing
import json


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
	print(cookies)

	#Then visit the json page for fetching the json
	actualurl='https://www.nseindia.com/api/underlying-information'
	res = s.get(actualurl,headers=headers,timeout=2)
	print(res.json())

	s.close()
	return res.json()

def main():
	underlying_info()

#Main program
if __name__ == '__main__':
	main()