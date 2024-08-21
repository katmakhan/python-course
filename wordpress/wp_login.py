#For invoking http requests
import requests

#Json Parsing
import json

#Date time
from datetime import datetime;


from urllib.parse import urlencode, quote

import random


def main():
	web_str=input("Enter the website:")
	login_str=input("Enter the id:")

	while True:
		pass_str=input("Enter the pass:")
		wp_login_method(web_str,login_str,pass_str)

def wp_login_method(website,loginid,loginpass):

	#Session to maintain the cookies
	s = requests.Session()

	headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}

	# website="https://something.in"
	# loginid="admin"
	# loginpass="admin123"
	# num = random.random()
	payload={
		"log":loginid,
		"pwd":loginpass,
		"wp-submit":"Log In",
		"redirect_to":website+"/wp-admin",
		# "testcookie": str(num)
	}


	loginurl=website+"/wp-login.php"

	# To get the cookie
	firstres=s.get(url=loginurl)
	print(firstres.cookies.get_dict())
	# s.cookies.set('wordpress_test_cookie', 'new_cookie_value')

	response=s.post(url=loginurl,headers=headers,data=payload)

	if 'wp-admin' in response.url:
		print("Sucess")
	else:
		# print(response.text)
		print("Password Incorrect")

	s.close()
	
#Main program
if __name__ == '__main__':
	main()