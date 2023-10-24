#For invoking http requests
import requests

#Json Parsing
import json


def main():

	#Visit the main page to bypass cookies
	#Session to maintain the cookies
	s = requests.Session()

	# # Headers for useragent
	# headers = {
	# "Accept-Encoding": "gzip, deflate, br",
	# "Accept-Language": "en-US,en;q=0.5",
	# "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
	
	stockname="m%26m"
	# stockname="RELIANCEs"
	# mainurl="https://chartink.com/stocks/"+stockname+".html"
	mainurl="https://chartink.com/search_stocks?term="+stockname
	response = s.get(mainurl,timeout=2)
	# print(response.text)

	if "stocksearch" in response.text:
		print("Found")
	else:
		print("No result found")
	

#Main program
if __name__ == '__main__':
	main()