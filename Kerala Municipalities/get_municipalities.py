import requests
from bs4 import BeautifulSoup
import json

def clean_text(text):
    return text.strip().replace('\n', '').replace('\r', '')

#Reading JSON
def readjson(location):
	print("Reading data from JSON File...",location)
	with open(location, 'r', encoding='utf-8') as f:
		stockdata=json.load(f)
		print("Sucessfully read json file")
		f.close()
		return stockdata

#Writing JSON
def writejson(location,jsondt):
	print("Writing data into JSON File...",location)
	with open(location, 'w+', encoding='utf-8') as f:
		json.dump(jsondt, f, ensure_ascii=False, indent=4)
		print("Sucessfully written into json file")
		print("\n")
		f.close()

def get_municipalities(id,name):
	url = "https://lsgkerala.gov.in/electionupdates/deStatusLB.php?distID="
	url=url+str(id)
	print("Fetching the data of ",name," ",id)
	response = requests.get(url)

	if response.status_code == 200:
		response.encoding = 'utf-8'  # Ensure proper encoding
		soup = BeautifulSoup(response.text, 'html.parser')
		table = soup.find('table', {'class': 'clsEngText'})

		data = []

		# Check if the table exists and extract rows
		if table:
			rows = table.find_all('tr')
			for row in rows:
				cols = row.find_all('td')
				cols = [clean_text(col.text) for col in cols]
				if cols:  # Skip empty rows
					data.append(cols)

		# Print the extracted data
		print("Extracted Data:")
		output={}
		for entry in data:
			# print(entry)
			if entry[1]!="Total" and entry[1]!="Localbody Name":
				output[entry[1]]={}
				# output[entry[1]]['districtId']=name
				output[entry[1]]['name']=entry[1]
				output[entry[1]]['wardCount']=int(entry[2])

		# print(output)
		return output

def get_totaldistricts():
	url="https://lsgkerala.gov.in/electionupdates/login.php"
	print("Fetching total district")
	response = requests.get(url)
	if response.status_code == 200:
		response.encoding = 'utf-8'  # Ensure proper encoding
		soup = BeautifulSoup(response.text, 'html.parser')
		table = soup.find('table', {'class': 'clsEngText'})

		data = []

		# Check if the table exists and extract rows
		if table:
			rows = table.find_all('tr')
			for row in rows:
				cols = row.find_all('td')
				cols = [col.text.strip() for col in cols]
				if cols:  # Skip empty rows
					data.append(cols)

		# Print the extracted data
		print("Extracted Data:")
		output={}
		for entry in data:
			# print(entry)
			if entry[1]!="District" and entry[1]!="Total":
				output[entry[1]]={}
				output[entry[1]]['name']=entry[1]
				output[entry[1]]['districtid']=entry[0]

		print(output)
		return output

totaldistrict=get_totaldistricts()
writejson("Data/Totaldistrict.json",totaldistrict)

totalresult={}
for district in totaldistrict:
	result=get_municipalities(totaldistrict[district]['districtid'],district)
	totalresult[district]={}		
	totalresult[district]=result
	# writejson("Data/"+district+".json",result)
writejson("Data/Totalresult.json",totalresult)
