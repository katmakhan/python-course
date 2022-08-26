# Proxy Rotation 
- Proxy are used to send requests from `different IP`
- Proxy enables you to acess `location specific` contents
- Proxy enables you for `data extraction`, as `IP gets blocked` for too many requests
- `Dedicated Proxy` is better than `FREE proxies`


### Sample for testing single proxy

```python
import requests

def check_proxy(proxy):
	try:
		testurl="https://httpbin.org/ip"
		print("Testing the IP Proxy ",proxy)

		test_resp=requests.get(testurl,proxies={'http':proxy,'https':proxy},timeout=3)
		print(test_resp.status_code)
		print(test_resp.json())
		print("Working")
		return proxy

	except:
		print("Proxy failed")
		pass
```

### Sample for testing multiple proxy in loop

```python
import csv

# Reading proxylist from csv file
proxylist=[]
with open('proxy-list.csv','r') as f:
	reader= csv.reader(f)
	for row in reader:
		proxylist.append(row[0])

print("Number of proxies in the CSV: ",len(proxylist))

#Checking if the Proxy IP is working or NOT
for proxy in proxylist:
	proxy_resp=check_proxy(proxy)
	if proxy_resp:
		print("The Proxy ",proxy," is working...")
		print("This proxy might not be stable or reliable like dedicated proxy, but works")
		break
```

### Download Proxy List from Internet
```python
from requests_html import HTMLSession

def collect_proxies(url):
	#NSE INDIA DERIVATIVE STOCK WATCH
	r=session.get(url)
	print("waiting to render...")
	r.html.render(sleep=1)
	tabledata = r.html.find("table#tbl_proxy_list",first=True)

	proxy_list=[]
	for tbody in tabledata.find("tbody"):
		for item in tbody.find("tr"):
			count=0

			ip=""
			port=""
			country=""

			for td in item.find("td"):
				# print(td.text)
				count=count+1

				if(count==1):
					ip=td.text
					# print(ip)

					if "adsbygoogle = window.adsbygoogle" in ip:
						break
					else:
						if ")))" in ip:
							ip=ip.split(")))")[1]
							# print("Ip: ",ip)
							
						if "))" in ip:
							ip=ip.split("))")[1]
							# print("Ip: ",ip)

				if(count==2):
					port=td.text
					# print("Port: ",port)
				if(count==6):
					country=td.text
					# print("Country: ",country)

			if ip is not "":
				proxy=str(ip)+":"+str(port)
				print(proxy)
				proxy_list.append(proxy)

	return proxy_list

# Reading Proxy from free proxy list from internet
session = HTMLSession()
print("Requesting Session")
proxy_url="https://www.proxynova.com/proxy-server-list/elite-proxies"
proxylist=collect_proxies(proxy_url)    

print("Number of proxies from internet: ",len(proxylist))

```