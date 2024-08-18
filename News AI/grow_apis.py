#For invoking http requests
import requests

#Json Parsing
import json

from PIL import Image
from io import BytesIO
import os


def nifty_intradaychart():
	actualurl='https://groww.in/v1/api/charting_service/v2/chart/delayed/exchange/NSE/segment/CASH/NIFTY/daily?intervalInMinutes=1&minimal=true'
	res = requests.get(actualurl,timeout=2)
	fnolistdata=res.json()
	# print(fnolistdata)
	return fnolistdata


def nifty_topoptions():
	
	actualurl='https://groww.in/v1/api/stocks_fo_data/v1/contracts/nifty/top'
	res = requests.get(actualurl,timeout=2)
	fnolistdata=res.json()
	# print(fnolistdata)
	return fnolistdata
 
# 500325
def get_icon_data(nse_number,stockname):
	actualurl=f'https://assets-netstorage.groww.in/stock-assets/logos/GSTK{nse_number}.png'
	res = requests.get(actualurl,timeout=2)

	if res.status_code == 404:
		print("Image not found for ",stockname)
		return
	# Open the image using Pillow
	image = Image.open(BytesIO(res.content))

	# Directory to save the downloaded image
	download_dir = "Stock_Icons"
	os.makedirs(download_dir, exist_ok=True)

	# Save the image to the local directory
	image_path = os.path.join(download_dir, f"{stockname}.png")
	image.save(image_path)

	print(f"Downloaded and saved GSTK{stockname}.png")
	
	
# def main():
# 	nifty_intradaychart()
	
# #Main program
# if __name__ == '__main__':
# 	main()