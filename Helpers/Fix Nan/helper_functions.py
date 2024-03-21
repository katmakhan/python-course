#Json Parsing
import json

#Time Parsing
from datetime import datetime
from datetime import timedelta
import time

#Deepcopy
from copy import deepcopy

import os
import shutil

import os
import math

def convert_nan_to_null(data):
    if isinstance(data, (float,)):
        if math.isnan(data):
            return None
    elif isinstance(data, dict):
        return {key: convert_nan_to_null(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [convert_nan_to_null(item) for item in data]
    else:
        return data

def checkdir_make(absolute_path):
	# Check if the directory already exists
	if not os.path.exists(absolute_path):
		# Create the directory
		os.makedirs(absolute_path)
		print(f"Directory '{absolute_path}' created successfully.")
	else:
		print(f"Directory '{absolute_path}' already exists.")

# convert to only needed dataset
def converttoohlc(data):
	output={}
	output['stckname']=data['stckname']
	output['pcnt']=data['pcnt']

	output['open'] = data['open']
	output['close']=data['close']
	output['high']=data['high']
	output['low']=data['low']
	output['vol']=int(data['vol'])
	return output

# Get timeinmill
def gettimeinmill():
	current_time_seconds = time.time()
	current_time_milliseconds = int(current_time_seconds * 1000)
	return current_time_milliseconds

# Get the directory of the current script
def getscriptdir():
	script_dir = os.path.dirname(os.path.realpath(__file__))
	print(script_dir)
	return script_dir

#show the time elapsed
def showelapsedtime(start_time,end_time,which):
	elapsed_time = end_time - start_time
	print("Elapsed Time for ",which," : {:.2f} seconds".format(elapsed_time))

#Convert date object to date string
def convert_to_date_obj(date_str,date_format):
	date_obj = datetime.strptime(date_str,date_format)
	return date_obj
# %d-%m-%Y %H:%M:%S
#Convert date string into date object
def convert_to_date_str(date_obj,date_format):
	date_str=date_obj.strftime(date_format)
	return date_str
	
#Conversion of date and time--------------------------------------------------------------
def convert_mil_todate(seconds,date_format):
	date_obj=datetime.fromtimestamp(int(seconds))+ timedelta(hours=5, minutes=30)
	date_str=date_obj.strftime(date_format)
	return date_str
	
#Conversion of date and time--------------------------------------------------------------
def current_milli_time():
	seconds=round(time.time())
	return seconds

def today():
	return datetime.now()

#Merge two dict
def dict_of_dicts_merge(x, y):
	z = {}
	overlapping_keys = x.keys() & y.keys()
	for key in overlapping_keys:
		z[key] = dict_of_dicts_merge(x[key], y[key])
	for key in x.keys() - overlapping_keys:
		z[key] = deepcopy(x[key])
	for key in y.keys() - overlapping_keys:
		z[key] = deepcopy(y[key])
	return z

#readfromdict
def readfromjson(fileloc):
	print("Reading json from ",fileloc)

	#From Dict
	# datalist=readdict("all_stock_data.json")

	#From Json
	datalist=readjson(fileloc)

	jsondata={}
	for data in datalist:
		print(data)
		historicallist=datalist[data]

		jsondata[data]={}
		for datedata in historicallist:
			date=datedata[0]
			open=datedata[1]
			high=datedata[2]
			low=datedata[3]
			close=datedata[4]
			vol=datedata[5]
			# print(date)

			jsondata[data][date]={}

			jsondata[data][date]['date']=date
			jsondata[data][date]['open']=open
			jsondata[data][date]['high']=high
			jsondata[data][date]['low']=low
			jsondata[data][date]['close']=close
			jsondata[data][date]['vol']=vol

	print("Returning json data..")
	return jsondata

def readdict(location):
	with open(location, 'r') as f:
		content = f.read()
		dictionary = ast.literal_eval(content)
		print("Sucessfully read dictionary file")
		f.close()
		return dictionary

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

#merge the updated list with new correct name after checking
def mergefirebaselist(firebaselist,stocks_array):

	newjson={}
	for stockf in firebaselist:
		# stocknamef=stockf
		stocknamef=stockf.split(":")[1].split("-")[0]

		found=False
		for stock in stocks_array:
			stockname=stock.split(":")[1].split("-")[0]

			if stocknamef==stockname:
				found=True
				newjson[stock]=100

		if found==False:
			newjson[stockf]=100

	return newjson

def convertonsedata(totalstocks,extension):
	totallist=[]
	for stock_symbol in totalstocks:
		if "NIFTY" not in stock_symbol and "INDIAVIX" not in stock_symbol and "CNX" not in stock_symbol:
			# totallist.append(("NSE:"+stock+"-EQ").replace("&","%26"))
			totallist.append("NSE:"+stock_symbol+"-"+extension)


	# print(totallist)
	return totallist

def convertobsedata(totalstocks,extension):
	totallist=[]
	for stock_symbol in totalstocks:
		if "NIFTY" not in stock_symbol and "INDIAVIX" not in stock_symbol and "CNX" not in stock_symbol:
			# totallist.append(("NSE:"+stock+"-EQ").replace("&","%26"))
			totallist.append("BSE:"+stock_symbol+"-"+extension)


	# print(totallist)
	return totallist

def removeextension(totalstocks):
	totallist=[]
	for stock in totalstocks:
		stock_symbol=stock.split(":")[1].split("-")[0]
		totallist.append(stock_symbol)

	# print(totallist)
	return totallist

def convertarraytojson(totalstocks):
	result={}
	for stockname in totalstocks:
		result[stockname]=100
	return result

def convertjsontoarray(totalstocks):
	totallist=[]
	for stock in totalstocks:
		# totallist.append(("NSE:"+stock+"-EQ").replace("&","%26"))
		totallist.append(stock)


	print(totallist)
	return totallist

def get_allfiles(location,extension):
	arr = os.listdir(location)
	fileslist=[]
	for file in arr:
		if extension in file:
			# print(file)
			fileslist.append(file)

	fileslist=sorted(fileslist)
	return fileslist

def deleteoldata(location):
	folderpath=os.path.join(os.getcwd(),location)
	try:
		shutil.rmtree(folderpath)
		print("Deleted the files in location...")
	except Exception as e:
		print('Failed to delete %s. Reason: %s' % (folderpath, e))
		print("No folder found")