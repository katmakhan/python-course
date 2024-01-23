#For invoking http requests
import requests

#Json Parsing
import json
import time 
missinglist_afer=['NSE:AMARAJABAT-EQ', 'NSE:BAJAJ-AUTO-EQ', 'NSE:BZUIPPP-BZ', 'NSE:GET%26D-BE', 'NSE:GISOLUTION-BE', 'NSE:GMRP%26UI-EQ', 'NSE:HCL-INSYS-EQ', 'NSE:HDFC-EQ', 'NSE:IDBIGOLD-EQ', 'NSE:IL%26FSENGG-BZ', 'NSE:J%26KBANK-EQ', 'NSE:JSWISPL-EQ', 'NSE:KEERTI-BZ', 'NSE:L%26TFH-EQ', 'NSE:LSIL-EQ', 'NSE:M%26M-EQ', 'NSE:M%26MFIN-EQ', 'NSE:MAESGETF-EQ', 'NSE:MAFSETF-EQ', 'NSE:MAGOLDETF-EQ', 'NSE:MAGS813ETF-EQ', 'NSE:MAM150ETF-EQ', 'NSE:MAMFGETF-EQ', 'NSE:MAN50ETF-EQ', 'NSE:MANV30F-EQ', 'NSE:MANXT50-EQ', 'NSE:MASILVER-EQ', 'NSE:MAXVIL-EQ', 'NSE:MCDOWELL-N-EQ', 'NSE:MRO-TEK-EQ', 'NSE:NAM-INDIA-EQ', 'NSE:ORIENTABRA-EQ', 'NSE:PROZONINTU-EQ', 'NSE:REVATHI-BE', 'NSE:SCAPDVR-BE', 'NSE:SEPOWER-BE', 'NSE:SUNCLAYLTD-EQ', 'NSE:SURANAT%26P-EQ', 'NSE:UCALFUEL-EQ']

def main():

	#Visit the main page to bypass cookies
	#Session to maintain the cookies
	s = requests.Session()

	# # Headers for useragent
	# headers = {
	# "Accept-Encoding": "gzip, deflate, br",
	# "Accept-Language": "en-US,en;q=0.5",
	# "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
	
	missinames=[]
	for stockname in missinglist_afer:
		# stockname="m%26m"
		# stockname="RELIANCEs"
		# mainurl="https://chartink.com/stocks/"+stockname+".html"
		stockname=stockname.split(":")[1].split("-")[0]
		mainurl="https://chartink.com/search_stocks?term="+stockname
		response = s.get(mainurl,timeout=2)
		# print(response.text)

		if "stocksearch" in response.text:
			print("Found ",stockname)
		else:
			print("No result found for ",stockname)
			missinames.append(stockname)

		time.sleep(1)
		
	print(stockname)

#Main program
if __name__ == '__main__':
	main()