#For invoking http requests
import requests

def main():

	#Visit the main page to bypass cookies
	#Session to maintain the cookies
	s = requests.Session()

	# Headers for useragent
	headers = {
	# "Accept-Encoding": "gzip, deflate, br",
	"Accept-Language": "en-US,en;q=0.5",
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}

	
	# To set the cookies, by visiting the mainpage
	mainurl = "https://www.amazon.in/"
	response = s.get(mainurl,headers=headers,timeout=2)
	# cookies = s.cookies
	# print(cookies)
	# print(response.text)
	# print("_________________________")
	# print("\n\n")


	#Then visit the json page for fetching the json
	# actualurl="https://data.amazon.in/api/marketplaces/A21TJRUUN4KGV/taxonomies/buyback/offers-for-category?encryptedProductMerchantId=A14CZOWI0VEHLG&productSubcategory=1805560031&asin=B09G9BL5CP&brand=Apple&rbnHierarchyNodes=1805560031&buybackCategory=&productPrice=50999"
	# actualurl="https://www.amazon.in/Apple-iPhone-13-128GB-Blue/dp/B09G9BL5CP"
	# actualurl="https://www.amazon.in/gp/product/ajax?asin=B09G9JJT7M&showFeatures=inEmiPopOver-fetch%2Cinemi&deviceType=desktop&experienceId=emiMenueSVAjaxExperience&merchantId=AUCQGA5A6IVIW"
	actualurl="https://www.amazon.in/s?k=iphone14"


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