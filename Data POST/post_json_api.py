#For invoking http requests
import requests

#Json Parsing
import json

	
def main():
	#For Testing
	url='https://w'
	
	#This website prevents normal Traffic, unlesss you specify the user agent, the server won't response
	resp = requests.put(url,headers=headers)
	print("Done..")
	print(resp)
	data = resp.json()	
	print(data)
	
#Main program
if __name__ == '__main__':
	main()