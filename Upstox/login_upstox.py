#For invoking http requests
import requests

#Json Parsing
import json

#Date time
from datetime import datetime;

from http.cookies import SimpleCookie

import uuid
import platform
from urllib.parse import urlencode, quote

# Custom Unique Key
from nanoid import generate

def main():

	#Session to maintain the cookies
	s = requests.Session()

	# Headers for content Type 
	headerslogin = {
	# "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
	# "Accept-Encoding":"gzip, deflate, br",
	# "Accept-Language":"en-US,en;q=0.9",
	# "Content-Type":"application/json",
	"Content-Type":"text/plain",
	# "Connection":"keep-alive",
	# "X-Device-Details":"platform=WEB|osName=Mac OS/10.15.7|osVersion=Brave/119.0.0.0|appVersion=4.0.0|modelName=Brave|manufacturer=Apple",
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
	

	# Define a custom alphabet
	alphabet = '1234567890abcdef'
	# Create a custom nanoid generator
	generated_id = generate(alphabet, 10)
	# generated_id="b9d084cce6"


	print("request id is ","WPRO-" + generated_id)

	headersotp = {
	# "Accept": "*/*",
    # 'Accept-Encoding': 'gzip, deflate, br',
    # 'Accept-Language': 'en-US,en;q=0.5',
	"Content-Type":"application/json",
	# "Content-Type":"text/plain",
	# "X-Request-Id":"WPRO-21e05771b2",
 # 	'Sec-Ch-Ua': '"Brave";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
 #    'Sec-Ch-Ua-Mobile': '?0',
 #    'Sec-Ch-Ua-Platform': '"macOS"',
 #    'Sec-Fetch-Dest': 'empty',
    # 'Sec-Fetch-Mode': 'cors',
    # 'Sec-Fetch-Site': 'same-site',
 #    'Sec-Gpc': '1',
	# 'authority': 'service.upstox.com',
	# "Origin":"https://login.upstox.com",
	# "Referer":"https://login.upstox.com/",
	"X-Request-Id": "WPRO-" + generated_id,
	# "X-Device-Details":"platform=WEB|osName=Mac OS/10.15.7|osVersion=Brave/119.0.0.0|appVersion=4.0.0|modelName=Brave|manufacturer=Apple",
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
	}
	

	timestamp=round(datetime.now().timestamp())
	print("timestamp: ",timestamp)

	# Payload Creation for OTP Generation
	mobilnum="9847437456"
	# mobilnum="<script>alert('gotcha!')</script>"
	payload={}
	payload['data']={}
	payload['data']['mobileNumber']=mobilnum
	print(payload)


	loginurl=f"https://upstoxpro.s3.ap-south-1.amazonaws.com/platform/web/post-trade/login-config.json?v={timestamp}"
	# loginurl="https://login.upstox.com"
	generateotp="https://service.upstox.com/login/open/v5/auth/1fa/otp/generate" # Need cookie
	engageurl=f"https://service.upstox.com/tracking-proxy/open/mp/events/engage/?verbose=1&ip=1&_={timestamp}"
	validateotp="https://service.upstox.com/login/open/v4/auth/1fa/otp-totp/verify"
	verifytoken="https://service.upstox.com/gateway-worker/v1/verify-access-token"
	clientinfo="https://service.upstox.com/profile/v4/client-info"

	# https://hashes.com/en/decrypt/hash

	# Checking login
	res=s.get(engageurl,headers=headerslogin)
	# print(res)
	# print(res.cookies.get_dict())
	cookies = res.cookies.get_dict()
	print("\n")
	print("Cookies Login-----")
	for data in cookies:
		print(data," : ",cookies[data])
	print("Cookies Login-----")
	# print(res.headers)

	# cookies['mp_62597aa51842e6e2c56b97d96e4c5f8a_mixpanel']=device_id

	# cookie_string="__cf_bm=mTNQxU6Ox8c4IaNotw3HiVsezPwXR77xncmyx1FOoX8-1700805086-0-AWbQijq2Vuhvi3yj68+mLN/DgD4I5zipKdjsvMtRmmYdUqmoS7kRDC/9sU34JmhSSYMoDwVINCbliMhTJZydGZs=; _cfuvid=mKjRy9ZoaXkTUa78kI2Ge6NGPdDoy4WPI7EBoa1Xl9Y-1700805086385-0-604800000; mp_62597aa51842e6e2c56b97d96e4c5f8a_mixpanel=%7B%22distinct_id%22%3A%20%22%24device%3A18bffe2102c610-090ad3ef54856b-16525634-b1a29-18bffe2102c610%22%2C%22%24device_id%22%3A%20%2218bffe2102c610-090ad3ef54856b-16525634-b1a29-18bffe2102c610%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%2C%22Platform%22%3A%20%22Web%203.0%22%7D; __cfruid=979d6a7653a34280130ea1b2a7a65a07a1ba9776-1700805087"
	# # Parse the cookie string into a SimpleCookie object
	# cookie = SimpleCookie()
	# cookie.load(cookie_string)

	# # Convert SimpleCookie to a dictionary
	# cookie_dict = {key: morsel.value for key, morsel in cookie.items()}

	# device_id = str(uuid.uuid4())
	# print(device_id)

	#%7B%22distinct_id%22%3A%20%22%24device%3A18c002c3b5d615-0bf7e2c6fd167e-16525634-12f096-18c002c3b5d615%22%2C%22%24device_id%22%3A%20%2218c002c3b5d615-0bf7e2c6fd167e-16525634-12f096-18c002c3b5d615%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%2C%22Platform%22%3A%20%22Web%203.0%22%7D
	#%7B%22distinct_id%22%3A%20%22%24device%3A18c002c3b5d615-0bf7e2c6fd167e-16525634-12f096-18c002c3b5d615%22%2C%22%24device_id%22%3A%20%2218c002c3b5d615-0bf7e2c6fd167e-16525634-12f096-18c002c3b5d615%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%2C%22Platform%22%3A%20%22Web%203.0%22%7D	
	device_id='18c002c3b5d615-0bf7e2c6fd167e-16525634-12f096-18c002c3b5d615'

	# Create a dictionary with the cookie data, including the dynamic device ID
	cookie_data = {
	    'distinct_id': '$device:18c002c3b5d615-0bf7e2c6fd167e-16525634-12f096-18c002c3b5d615',
	    '$device_id': '18c002c3b5d615-0bf7e2c6fd167e-16525634-12f096-18c002c3b5d615',
	    '$initial_referrer': '$direct',
	    '$initial_referring_domain': '$direct',
	    'Platform': 'Web 3.0'
	}

	encoded_cookie = quote(str(cookie_data))


	# # mixpanel="mp_62597aa51842e6e2c56b97d96e4c5f8a_mixpanel"
	cookies['mp_62597aa51842e6e2c56b97d96e4c5f8a_mixpanel']=encoded_cookie.replace("%27", "%22").replace("2C%20%22","2C%22")
	# print(cookies)
	print("\n")
	print("Cookies OTP-----")
	for data in cookies:
		print(data," : ",cookies[data])
	print("Cookies OTP-----")
	print("\n")


	# Check OTP Generation
	# genotp=s.post(url=generateotp,headers=headersotp,data=payload,cookies=cookie_dict)
	# genotp=s.post(url=generateotp,headers=headerslogin,data=payload)
	genotp=s.post(url=generateotp,headers=headersotp,data=payload,cookies=cookies)
	# print(genotp)
	# print(genotp.cookies.get_dict())
	print(genotp.text)
	# print(genotp.json())
	# print(genotp.headers)

	# s.close()
	
#Main program
if __name__ == '__main__':
	main()