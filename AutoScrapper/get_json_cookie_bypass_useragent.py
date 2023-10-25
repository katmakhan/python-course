#For invoking http requests
import requests

#Json Parsing
import json

#Parsing
from bs4 import BeautifulSoup

#regEx
import re


def find_token(javascript_code):
	# Define a regex pattern to match the 'token' value
	token_pattern = r"'token'\s*:\s*\"([^\"]*)\""
	# Use regex to search for the 'token' value
	match = re.search(token_pattern, javascript_code)
	if match:
		token_value = match.group(1)
		print("Token:", token_value)
		return token_value
	else:
		print("Token not found in the JavaScript code.")
	print("_________________")

def find_requestId(javascript_code):
	# Define a regex pattern to match the 'requestId' value
	request_id_pattern = r'requestId: "([^"]*)"'

	# Use regex to search for the 'requestId' value
	match = re.search(request_id_pattern, javascript_code)

	if match:
		request_id_value = match.group(1)
		print("requestId:", request_id_value)
		return request_id_value
	else:
		print("requestId not found in the JavaScript code.")

def find_exp(javascript_code):
	# Define a regex pattern to match the desired text
	pattern = r'exp=([^&]+)'

	# Use regex to search for the text
	match = re.search(pattern, javascript_code)

	if match:
		extracted_text = match.group(1)
		print("Extracted text:", extracted_text)
		return extracted_text
	else:
		print("Text not found in the JavaScript code.")

def main():

	#Visit the main page to bypass cookies
	#Session to maintain the cookies
	s = requests.Session()

	# Headers for useragent
	headers = {
	"Accept-Encoding": "gzip, deflate, br",
	"Accept-Language": "en-US,en;q=0.5",
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}

	
	# To set the cookies, by visiting the mainpage
	mainurl = "https://www.amazon.in/"
	response = s.get(mainurl,timeout=2)
	# cookies = s.cookies
	# print(cookies)
	# print(response.text)
	# print("_________________________")
	# print("\n\n")

	soup = BeautifulSoup(response.text,'html.parser')
	# Find all <script> tags
	script_tags = soup.find_all('script')
	# print(script_tags)

	token=""
	reqid=""
	exp=""

	for scripts in script_tags:
		# print(scripts)
		# print("________________")

		if "a9_sl_sessionCacheUpdateHandler" in scripts.text:
			# print("Found the <token>")
			# print(scripts.text)
			token=find_token(scripts.text)
		

		if "completion.amazon.co.uk/search/complete" in scripts.text:
			# print("Found <requestId>")
			# print(scripts.text)
			# print("_________________")
			reqid=find_requestId(scripts.text)

		if "/ah/ajax/counter?ctr=desktop_ajax_at" in scripts.text:
			# print("Found <exp>")
			# print(scripts.text)
			# print("_________________")
			exp=find_exp(scripts.text)



	#Then visit the json page for fetching the json
	# actualurl="https://data.amazon.in/api/marketplaces/A21TJRUUN4KGV/taxonomies/buyback/offers-for-category?encryptedProductMerchantId=A14CZOWI0VEHLG&productSubcategory=1805560031&asin=B09G9BL5CP&brand=Apple&rbnHierarchyNodes=1805560031&buybackCategory=&productPrice=50999"
	actualurl="https://www.amazon.in/Apple-iPhone-13-128GB-Blue/dp/B09G9BL5CP&pf_rd_r="+reqid
	# actualurl='https://www.amazon.in/s?k=iphones'
	# actualurl = "https://www.amazon.in/gp/product/sessionCacheUpdateHandler.html"
	# actualurl= "https://unagi.amazon.in/1/events/com.amazon.eel.SearchAutocompleteUIServiceMetrics.nexus"
	# actualurl= "https://unagi.amazon.in/1/events/com.amazon.csm.csa.prod"
	res = s.get(actualurl,headers=headers,timeout=2)
	print(res.text)
	print("Found ")

	s.close()

	
#Main program
if __name__ == '__main__':
	main()