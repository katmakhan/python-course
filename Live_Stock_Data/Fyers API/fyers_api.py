#importing the os module
import os
from sys import platform

#To get the current working directory
directory = os.getcwd()

#Fyers Model
from fyers_api import fyersModel
from fyers_api import accessToken
from fyers_api.Websocket import ws

#For invoking http requests
import requests
# Converting text to url encode for links
import urllib.parse

#Json Parsing
import json
#Time Parsing
from datetime import datetime
from datetime import timedelta
import time


#Firebase
import firebase_admin.messaging as messaging
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import auth

#firebaseval={<Your Json credential you get from project settings>}
firebaseval={
  "type": "service_account",
  "project_id": "<Project Name>",
  "private_key_id": "<id>",
  "private_key":"<key>",
  "client_email": "firebase-adminsdk@<Project ID>.iam.gserviceaccount.com",
  "client_id": "<Clinet id>",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-ipcf5%40<Project Name>.iam.gserviceaccount.com"
}
cred = credentials.Certificate(firebaseval)

print("\n---------------------------")
print("Initialising Firebase...")

db1_url='https://<Your Project Name>-<Database Name>.firebaseio.com/'
db2_url='https://<Your Project Name>-<Database Name>.firebaseio.com/'
db3_url='https://<Your Project Name>-<Database Name>.firebaseio.com/'
#Initilising Database 1- fetching stock and option details
firebase_admin.initialize_app(cred, {
    'databaseURL' : db1_url
})

# Initilising Database 2- Updating the realtime data feed
app2 = firebase_admin.initialize_app(cred, {
    'databaseURL': db2_url
}, name='app2')

# Initilising Database 3- Fetching the nifty 50 values
app3 = firebase_admin.initialize_app(cred, {
    'databaseURL': db3_url
}, name='app3')

print("Initialised Firebase")
print("---------------------------\n")

#Convert date object to date string
def convert_to_date_obj(date_str,date_format):
	date_obj = datetime.strptime(date_str,date_format)
	return date_obj

#Convert date string into date object
def convert_to_date_str(date_obj,date_format):
	date_str=date_obj.strftime(date_format)
	return date_str
	
#Conversion of date and time--------------------------------------------------------------
def convert_mil_todate(seconds,date_format):
	date_obj=datetime.fromtimestamp(seconds)+ timedelta(hours=5, minutes=30)
	date_str=date_obj.strftime(date_format)
	return date_str

#Conversion of date and time--------------------------------------------------------------
def current_milli_time():
	seconds=round(time.time())
	return seconds
	
#RTD Location For fetching the data stored in the RTD
#API Keys
#Stock Names
#Index Names
#FNO Details will be fetched in REALTIME Using the Yesterdays Closing Price of Stocks

#api_child_name='api_key_fno'
#api_child_name='api_key_index'
api_child_name='api_key_stock'
		
api_loc='API'
live_rtd_loc='L'
live_rtd_loc_child="S"
rtd_loc='L2'
date_str=convert_to_date_str(datetime.now(),"%d-%B-%y")
index_loc='L'
index_loc_child="I"


	
# Update DB- Updating Live data
global empty_list_index
global empty_list_stock
global empty_list_fno
global expdate

empty_list_index={}
empty_list_stock={}
empty_list_fno={}

#in seconds
time_refresh_delay=3 

# Storing data set temporarily
global stocklist_bulk
stocklist_bulk={}

# Storing the range data (5-10 mints)
range_storage=1

# Converting to seconds
range_storage=range_storage*60
#range_storage=10

# Last updated range
global last_range
last_range=0

#Storing in RTD in BULK
#Stocklist[Range][stockname][TIME][VALUE]
#L2>INDEX>DATE>[RANGE]>STOCKNAME>TIME>VALUE

#Writing to LIVE RTD
#LIVE>S>STOCKNAME>VALUE
#LIVE>I>INDEXNAME>VALUE


#checktime=199852325 in seconds
#stockname=NIFTY50
#stockdata={NIFTY50:12000}

#5*60 =300 seconds

#1656491000 -8:23:20 AM
#1656491005 -8:23:25 AM

#1656489900- 8:05:00 AM % 300 = 0
#1656490000- 8:06:40 AM % 300 = 100
#1656490060- 8:07:40 AM % 300 = 200

#1656490300- 8:11:40 AM % 300 = 100

telegram_heading="FYERS API - Stock"


# Fyers API Dashboard , MY APP Details
app_id="XXXXXXXXX-100"
app_secret="XXXXXXXXX"
	

#Storing it in temp json, for bulk writes, to avoid extensive Data usage
def store_data_temp(ref,stockdata,checktime,stockname):
	global stocklist_bulk
	global last_range
		
	#Convert time to lower value
	diff=checktime%range_storage
	lower_range=checktime-diff
	print("Storing in the bulk")
	
	# Create the lower range if doesn't exist
	if stocklist_bulk.get(lower_range) is None:
		#print("Creating the lower range for the first time")
		stocklist_bulk[lower_range]={}
	
	# Create the stock under lower range if doesn't exist	
	if stocklist_bulk[lower_range].get(stockname) is None:
		#print("Creating the stock name for the first time in the lower range")
		stocklist_bulk[lower_range][stockname]={}
		
	# Create the time period under stock under lower range if doesn't exist	
	# DOnt use checktime 10 Digits, Just use last 4 significant digits
	checktime=str(checktime)[6:]
	
	if stocklist_bulk[lower_range][stockname].get(checktime) is None:
		#print("Creating the time period under stock name for the first time in the lower range")
		stocklist_bulk[lower_range][stockname][checktime]={}
		
	#Dont update with stockdata which contains the stock name again
	#Update with the value inside the stockname
	stocklist_bulk[lower_range][stockname][checktime]=stockdata[stockname]
	
	#Updating the last range for the first time
	if last_range==0:
		#print("Updating the lower range for the first time")
		last_range=lower_range
		
	# Check if new range is generated
	# lower_range is not equal to previous_lower_range
	# Then Update the DB
	else:
		if last_range!=lower_range:
			#Update the rtd bulk
			ref.child(str(last_range)).set(stocklist_bulk[last_range])
			print("------------------------------------------------------------------------")
			print("------------------------------------------------------------------------")
			print("Updated the range in the database")
			print(stocklist_bulk)
			print("------------------------------------------------------------------------")
			print("------------------------------------------------------------------------")
			
			#Set the new last range
			last_range=lower_range
			stocklist_bulk[last_range].clear()
			print("Clearing the bulk data")
	
	print("Finished the bulk")
	
#Need to check	
#Updating the Firebase Database	
def update_db(segment,stockname,value,date_str,checktime):
	#timeinmil=int(round(time.time()*1000))
	#12-05-22/NIFTY/165656/
	#ref=db.reference('L',app2).child(segment).child(date_str).child(stockname).child(str(checktime))
	ref=db.reference(rtd_loc,app2).child(segment).child(date_str)
	
	stockdata={}
	stockdata[stockname]=value
	
	#Only update in 3 seconds
	#Stocks
	global empty_list_index	
	global empty_list_stock
	global empty_list_fno

	if segment=="EQ":
		if not empty_list_stock[stockname]['flag']:
			#print("flag is false for stock")
			##############################################################################################################
			store_data_temp(ref,stockdata,checktime,stockname)
			#ref.set(stockdata)
			##############################################################################################################
			#print("Updated the rtd")
			empty_list_stock[stockname]['flag']=True
		else:
			#Check the time gap
			#print("flag is true for stock")
			if (checktime-empty_list_stock[stockname]['lasttime'] >time_refresh_delay):
				#print("3 seconds over, update it stocks")
				empty_list_stock[stockname]['flag']=False
				##########################################################################################################
				store_data_temp(ref,stockdata,checktime,stockname)
				#ref.set(stockdata)
				##########################################################################################################
				#print("Updated the rtd")
				empty_list_stock[stockname]['lasttime']=checktime
			else:
				print("Waiting.....")
				
		
	#Index	
	if segment=="EX":
		if not empty_list_index[stockname]['flag']:
			#print("flag is false for index")
			store_data_temp(ref,stockdata,checktime,stockname)
			#ref.set(stockdata)
			print("Updated the rtd")
			empty_list_index[stockname]['flag']=True
		else:
			#print("flag is true for index")
			
			#Check the time gap
			#print("Last recorded time: "+str(empty_list_index[stockname]['lasttime']))
			#print("Check Time: "+str(checktime))
			#print("Difference is: "+str(empty_list_index[stockname]['lasttime']-checktime))
			if (checktime-empty_list_index[stockname]['lasttime'] >time_refresh_delay):
				empty_list_index[stockname]['flag']=False
				#print("3 seconds over, update it index")
				store_data_temp(ref,stockdata,checktime,stockname)
				#ref.set(stockdata)
				print("Updated the rtd")
				empty_list_index[stockname]['lasttime']=checktime
			else:
				print("Waiting.....")
			

	
	#FNO	
	
	#print(empty_list_fno)
	if segment=="CE" or segment=="PE":
		#print("\n\n",stockname,"\n\n")
		if not empty_list_fno[stockname]['flag']:
			#print("flag is false for index")
			store_data_temp(ref,stockdata,checktime,stockname)
			#ref.set(stockdata)
			print("Updated the rtd")
			empty_list_fno[stockname]['flag']=True
		else:
			print("flag is true for index")
			
			#Check the time gap
			#print("Last recorded time: "+str(empty_list_fno[stockname]['lasttime']))
			#print("Check Time: "+str(checktime))
			#print("Difference is: "+str(empty_list_index[stockname]['lasttime']-checktime))
			if (checktime-empty_list_fno[stockname]['lasttime'] >time_refresh_delay):
				empty_list_fno[stockname]['flag']=False
				#print("3 seconds over, update it index")
				store_data_temp(ref,stockdata,checktime,stockname)
				#ref.set(stockdata)
				print("Updated the rtd")
				empty_list_fno[stockname]['lasttime']=checktime
			else:
				print("Waiting.....")
	
	
# Fetch DB- Fetching latest api
def fetch_fyers_auth_token():	
	ref = db.reference(api_loc,app2)
	latest_access_token=ref.get();
	return latest_access_token
	
# Fetch DB- Fetching nifty 50 stock details
def fetch_nifty50_stockdetails(fyers):	
	ref = db.reference(live_rtd_loc,app3)
	nifty50_stocks_list=ref.child(live_rtd_loc_child).get();
	
	stocks_array=[]
	
	for stock in nifty50_stocks_list:
		#Checking if all the names of the stocks are valid or not
		#print("Checking "+stock)
		#fetch_quote_data(fyers,"NSE:"+stock+"-EQ")
		#print("Checked")
		#print("--------")
		
		#Adding only then
		stocks_array.append(("NSE:"+stock+"-EQ").replace("&","%26"))
	
	#Removing INFRATEL
	stocks_array.remove('NSE:INFRATEL-EQ')
	return stocks_array
	
# Fetch DB- Fetching Index details
def fetch_index_details():
	ref = db.reference(index_loc,app3)
	index_list=ref.child(index_loc_child).get();
	
	index_array=[]
	for index_name in index_list:
		index_array.append(("NSE:"+index_name.replace(" ","")+"-INDEX").replace("&","%26"))
	
	return index_array	

# Fetch Option Details of Bank nifty and Nifty as an Array
def fetch_option_details(fyers):	
	global expdate
	today_str=convert_mil_todate(current_milli_time(),'%Y-%m-%d')
	today_str=convert_mil_todate(current_milli_time(),'%Y-%m-%d')
	
	#nifty50_ltp=fetch_history_data_format1(fyers,"NSE:NIFTY50-INDEX","D",today_str,today_str)
	#banknifty_ltp=fetch_history_data_format1(fyers,"NSE:NIFTYBANK-INDEX","D",today_str,today_str)
	
	nifty50_ltp=fetch_quote_data(fyers,"NSE:NIFTY50-INDEX")
	banknifty_ltp=fetch_quote_data(fyers,"NSE:NIFTYBANK-INDEX")
	
	if nifty50_ltp is None:
		update_telegram("Data Missing in Fyers API","There is no data for nifty 50 fyers")
	if banknifty_ltp is None:
		update_telegram("Data Missing in Fyers API","There is no data for Bank Nifty in fyers")
		
	options_total=[]
	
	if nifty50_ltp is not None and banknifty_ltp is not None:
	
		# Fetch 8 Nearby Nifty 50 options in both PE nd CE
		# Because we have 20 Indices in RTD
		# Fetch 7 Neatby Banknifty option in both PE and CE
		# 20+16+14 =50
		
		# Nifty have 100 Difference 
		# Bank Nifty have also 100 Difference
		
		# Options["BNIFTY"]
		# Options["NIFTY50"]
		
		nifty_ltp=int(nifty50_ltp['prev_close_price'])
		bank_ltp=int(banknifty_ltp['prev_close_price'])
		print("LTP Of Nifty 50: ",nifty_ltp)
		print("LTP Of BankNifty: ",bank_ltp)
		
		nifty_ltp=round(nifty_ltp,-2)
		bank_ltp=round(bank_ltp,-2)
		
		print("LTP Of Nifty 50 Rounded: ",nifty_ltp)
		print("LTP Of BankNifty Rounded: ",bank_ltp)
		
		#Nifty array
		nifty_arraylist=[]
		for i in range (-4,4):
			newltps=nifty_ltp+(i*100)
			nifty_arraylist.append(newltps)
			
		nifty_arraylist_CE=[]
		nifty_arraylist_PE=[]
		
		#Nifty array for CE is asc
		nifty_arraylist_CE=nifty_arraylist.copy()
		#Nifty array for PE is desc
		nifty_arraylist.reverse()
		nifty_arraylist_PE=nifty_arraylist
		
			
		#Bank Nifty array
		banknifty_arraylist=[]
		for i in range (-3,3):
			newltps=bank_ltp+(i*100)
			banknifty_arraylist.append(newltps)
			
		banknifty_arraylist_CE=[]
		banknifty_arraylist_PE=[]
		
		#Nifty array for CE is asc
		banknifty_arraylist_CE=banknifty_arraylist.copy()
		#Nifty array for PE is desc
		banknifty_arraylist.reverse()
		banknifty_arraylist_PE=banknifty_arraylist
		
		#Printing both ce and pe of both nifty and banknifty
		
		print("Nifty CE options is ",nifty_arraylist_CE)
		print("Nifty PE options is ",nifty_arraylist_PE)
		
		print("BankNifty CE options is ",banknifty_arraylist_CE)
		print("BankNifty PE options is ",banknifty_arraylist_PE)
		
		
		#Expiry date fetched from firebase
		# THis is a frecking array not dictionary, mayyrr
		all_expiry=db.reference("ED").get()
		latest_expiry_obj=convert_to_date_obj(all_expiry[0]['exp'],"%d-%b-%Y")
		
		#Iterate through the expiry
		current_date_obj=datetime.now()
		for expiry in all_expiry:
			print(expiry)
			date_obj=convert_to_date_obj(expiry['exp'],"%d-%b-%Y")
			if date_obj<latest_expiry_obj and date_obj>=current_date_obj:
				latest_expiry_obj=date_obj
				
		#Check if the latest expiry date object is less than 7 days
		#If the date is greater than 7 days, that means we calculated wrong expiry
		#Update the information in the firebase rtd
		
		latest_expiry_str=""
		# Os Finder
		if platform == "darwin" or platform=="linux":
			print("mac or unix...")
			latest_expiry_str=convert_to_date_str(latest_expiry_obj,"%y%-m%d")
			
		elif platform == "win32":
			print("windows")
			latest_expiry_str=convert_to_date_str(latest_expiry_obj,"%y%#m%d")
			
		# NIFTY+2022-APRIL-21+STRIKE
		# NIFTY+22421+STRIKE
		# 16200
		# 08722
		# CE
		# NIFTY0872216200CE
		# data = {"symbols":"NSE:NIFTY2271416200CE"}

		#14-7-22 is the sample expiry
		#22-7-14
		#22714
		print("Latest Expiry is: ",convert_to_date_str(latest_expiry_obj,"%b-%d"))
		print("Latest Expiry is: ",latest_expiry_str)
		expdate=latest_expiry_str
		
		
		#nifty_arraylist_CE
		#nifty_arraylist_PE
		#banknifty_arraylist_CE
		#banknifty_arraylist_PE
		
		#Adding Extra Bits of Information to all the options
		nifty_ce=add_extra_bits(nifty_arraylist_CE,"NSE:NIFTY"+latest_expiry_str,"CE")
		nifty_pe=add_extra_bits(nifty_arraylist_PE,"NSE:NIFTY"+latest_expiry_str,"CE")
		
		banknifty_ce=add_extra_bits(banknifty_arraylist_CE,"NSE:BANKNIFTY"+latest_expiry_str,"CE")
		banknifty_pe=add_extra_bits(banknifty_arraylist_PE,"NSE:BANKNIFTY"+latest_expiry_str,"PE")
		
		#Printing all
		#print("\n\n",nifty_ce)
		#print("\n\n",nifty_pe)
		
		#print("\n\n",banknifty_ce)
		#print("\n\n",banknifty_pe)
		
		#Adding all
		options_total=nifty_ce+nifty_pe+banknifty_ce+banknifty_pe
		#print(options_total)
	else:
		print("Data missing in Either Nifty or Bank Nifty or BOTH")
		
	
	return options_total	
	
# Adding extra bits before and after , for fyers syntax
# NSE:BANK + 31600 + CE
def add_extra_bits(array_list,before,after):
	temp_dictionary=[]
	for options in array_list:
		temp_dictionary.append(before+str(options)+after)
	
	return temp_dictionary
	
# Sent notification to telegram group
def update_telegram(title,body):
	#Bot Name: Your_Bot_Name
	#If you don't have one, create one using botfather
	#Create BOTS using https://t.me/botfather
	#Put a unique profile pic for bot, for uniqueness
	#Get the http api
	http_api="00000000000:ABCDXXXXXXXXXXXXXX-XXXXXXXXXXXX"

	#Add the bot to the group
	#Then go to this link to get the latest updates of the bot
	#https://api.telegram.org/bot<http_api>/getUpdates
	#https://api.telegram.org/bot00000000000:ABCDXXXXXXXXXXXXXX-XXXXXXXXXXXX/getUpdates
	#Find the group id from updates "chat":{"id":-12345678"
	chat_id="-12345678"


	messageurl1="https://api.telegram.org/bot"+http_api+"/sendMessage?chat_id="+chat_id+"&text="

	msg1=messageurl1+title+"\n\n"+body
	requests.get(msg1)
	print("Successfully sent the message")
	
def initialise_fyers():
	print("\n---------------------------")
	print("Initialising Fyers...")
	
	#appIdHash =SHA 256 of (appid+App Secret)
	#https://emn178.github.io/online-tools/sha256.html
	#appIdHash="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

	#For testing purpose
	redirect_url="https://trade.fyers.in/api-login/redirect-uri/index.html"
	unique_state="key123"
	responsetype="code"
	grant_type="authorization_code"
	
	session=accessToken.SessionModel(client_id=app_id,
	secret_key=app_secret,redirect_uri=redirect_url, 
	response_type=responsetype, grant_type=grant_type,
	state=unique_state)
	
	print("Initialised Fyers")
	print("---------------------------\n")
	return session
	
def generate_auth_url(app_id,redirect_url,unique_state):
	print("Generating Auth url...")
	
	# Genrating link for auth code generation
	url_for_Genrating_authcode="https://api.fyers.in/api/v2/generate-authcode?client_id="+app_id+"&redirect_uri="+redirect_url+"&response_type=code&state="+unique_state
	#print("Auth URL: "+url_for_Genrating_authcode)
	#print("\n")

	print("Generated the url!")
	return url_for_Genrating_authcode

def check_auth_token(session,auth_code):
	# # Link to generate auth Code
	#response_url = session.generate_authcode()
	#print("This will be the link "+response_url)

	#Result will be like
	# https://btechtraders.com/?s=ok&code=200&auth_code=ABCDxxxxxxxxxxxxXYZ&state=check_value123
	# From this get the auth code
	#auth_code="""
	#ABCDxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxXYZ
	#"""
	auth_code=auth_code.strip()

	# Validating Auth Code
	# Method 1
	# Using URL
	# url_for_Validating_authcode="https://api.fyers.in/api/v2/validate-authcode?grant_type=authorization_code"+"&appIdHash="+appIdhash+"&code="+auth_code
	# url_for_Validating_authcode="https://api.fyers.in/api/v2/validate-authcode?response_type=authorization_code"+"&appIdHash="+appIdHash+"&code="+auth_code

	# print("Validation URL: "+url_for_Validating_authcode)
	# grant_type":"authorization_code","appIdHash":"xxxxxxxxxxxxxxxxx","code":"eeeeeeeeeeeeeeeeeeeee"
	 
	# Method 2
	# Using Python
	access_token=""
	session.set_token(auth_code)
	session.secret_key
	response = session.generate_token()

	if response.get("access_token")!=None:
	  access_token = response["access_token"]
	  print("Acess Token is valid")
	  return access_token
	else:
	  print(response['message'])
	  new_url=generate_auth_url(session.client_id,session.redirect_uri,session.state)
	  update_telegram(telegram_heading,"Click on here to authenticate: "+urllib.parse.quote_plus(new_url))
	  
	  return None
  	
def fetch_history_data_format1(fyers,symbol_name,res,from_range,to_range):
	#set cont flag 1 for continues data and future options.
	cont_flag="0"	
	dataformat1 = {"symbol":symbol_name,"resolution":res,"date_format":"1","range_from":from_range,"range_to":to_range,"cont_flag":cont_flag}	
	data_set=fyers.history(dataformat1)

	print("\n--------------------------------------------------")
	if data_set['candles']!=[]:
	  all_candles=data_set['candles']
	  for candles in all_candles:
		  candles[0]=convert_mil_todate(candles[0],'%b-%d-%Y %#I:%M %p').split(" ")[1]
		  print(candles)
		  
	else:
	  print("No Data from fyers")
	
	print("--------------------------------------------------\n")

def fetch_history_data_format2(fyers,symbol_name,res,from_range,to_range):
	#set cont flag 1 for continues data and future options.
	cont_flag="0"	
	dataformat2 = {"symbol":symbol_name,"resolution":res,"date_format":"0","range_from":from_range,"range_to":to_range,"cont_flag":cont_flag}
	data_set=fyers.history(dataformat2)

	print("\n--------------------------------------------------")
	if data_set['candles']!=[]:
	  all_candles=data_set['candles']
	  for candles in all_candles:
		  candles[0]=convert_mil_todate(candles[0],'%b-%d-%Y %#I:%M %p').split(" ")[1]
		  print(candles)
		  
	else:
	  print("No Data from fyers")
	
	print("--------------------------------------------------\n")
	 
def fetch_quote_data(fyers,symbol):
	data = {"symbols":symbol}
	data=fyers.quotes(data)
	
	print("\n--------------------------------------------------")
	if data['s']!="error":
		livedata=data['d'][0]['v']
		#print(livedata)

		fetched_date=convert_mil_todate(livedata['tt'],'%Y-%m-%d')
		#print(fetched_date)
		todays_date=convert_mil_todate(current_milli_time(),'%Y-%m-%d')
		#print(todays_date)

		if(fetched_date.split(" ")[0]==todays_date.split(" ")[0]):
			print("Same Date")
		else:
			print("Different Dates")
			update_telegram("Different Dates","Error in Fyers API python")
			
		return livedata

	else:
		print(data['message'])
		return None
	print("--------------------------------------------------\n")
	
def fetch_indepth_data(fyers,symbol):
	print("\n--------------------------------------------------")
	data = {"symbol":symbol,"ohlcv_flag":"1"}
	data=fyers.depth(data)['d'][symbol]
	print("--------------------------------------------------\n")

#Where the listeners for the sockets are connected
def custom_message(msg):
	global date_str
	global expdate
	try:
		#print(msg)
		msg_string = json.dumps(msg[0])
		msg_json = json.loads(msg_string)
		
		if msg_json.get('symbol') is None:
			print("Error is parsing symbol")
			update_telegram("Symbol Error","Error is parsing symbol")
		else:
			temp_symbol=msg_json['symbol']
			temp_ltp=msg_json['ltp']
			
			print(temp_symbol+" @ "+str(temp_ltp))
			
			#If Stockname or Index
			#stock_name=msg_json['symbol'].split(":")[1].split("-")[0]
			#segment=msg_json['symbol'].split(":")[1].split("-")[1]
			
			#If Options
			stock_name=temp_symbol.split(":")[1].split(expdate)[0]
			temp_strike_op=temp_symbol.split(":")[1]
			
			#Segment is CE and PE when its Options
			#Segment is EX when its Index
			#Segment is EQ when its Stock
			segment=temp_strike_op[len(temp_strike_op)-2:]

			#If it is Index
			#Stock name will be NIFTY50-INDEX
			if segment=="EX":
				stock_name=stock_name.split("-")[0]
				
			#If it is Stock
			#Stock name will be RELIANCE-EQ
			if segment=="EQ":
				stock_name=stock_name.split("-")[0]
				
			if segment=="CE" or segment=="PE":
				strike_name=temp_strike_op.split(expdate)[1]
				strike_name=strike_name[:len(strike_name)-2]
				
				#Update the stockname
				stock_name=stock_name+expdate+strike_name+segment
				
			
			check_time=msg_json['timestamp']
			
			update_db(segment,stock_name,msg_json['ltp'],date_str,check_time)
			print(stock_name," ",segment," ",check_time)
			print("------------------------------------")
	
	except:
		print("Parsing Error")
		update_telegram("Parsing Error","Fyers API python"+"\n\n"+str(msg))
		pass
		
def disconnect_socket(fyersSocket,custom_list):
	data_type="symbolData"	
	try:
		fyersSocket.unsubscribe(symbol=custom_list)
		print("Done")
	except:
		print("Error here")
		
#For storing the last time bulk data updated
def create_empty_holder(stock_name_list):
	empty_list={}
	
	for stocks in stock_name_list:
		empty_list[stocks]={}
		
		empty_list[stocks]['flag']=False
		empty_list[stocks]['lasttime']=current_milli_time()
		
	return empty_list

# Remove Extra for only stock and Index Details
def remove_extra(stock_list_array):
	new_list_array=[]
	for stock in stock_list_array:
		new_name=stock.split(":")[1].split("-")[0]
		new_list_array.append(new_name)
	return new_list_array
	
# For subscribing to Stock Only- This
def fetch_live_data(fyers,fyersSocket):
	# log_path here is configurable this specifies where the output will be stored for you if the process is running in background
	#  fyersSocket = ws.FyersSocket(access_token=access_token,run_background=False,log_path=’home/Documents”)

	data_type="symbolData"
	#custom_list= []
	#nifty50_symbol= ["NSE:SBIN-EQ","NSE:ONGC-EQ"]
	#test_list= ['NSE:NIFTY50-INDEX','NSE:NIFTYBANK-INDEX']
	#index_list=fetch_index_details()
	stock_list=fetch_nifty50_stockdetails(fyers)
	#options_list=fetch_option_details(fyers)
	
	################################################################################# Real Deal
	fyersSocket.websocket_data = custom_message
	
	#print(index_list)
	#print("Subscribing to Index List")
	#fyersSocket.subscribe(symbol=index_list,data_type=data_type)
	
	#MAKE A DICTIONARY TO DELAY RTD UPDATION
	#index_list_without=remove_extra(index_list)
	stock_list_without=remove_extra(stock_list)
	#fno_list_without=remove_extra(options_list)
	
	#global empty_list_index
	global empty_list_stock
	#global empty_list_fno

	#empty_list_index=create_empty_holder(index_list_without)
	empty_list_stock=create_empty_holder(stock_list_without)
	#empty_list_fno=create_empty_holder(fno_list_without)
	
	#print(empty_list_index)
	#print(empty_list_stock)
	
	#print(stock_list)
	print("\n\n")
	print("Subscribing to Stock List\n")
	
	################################################################################# Real Deal
	fyersSocket.subscribe(symbol=stock_list,data_type=data_type)


	# If run_background Process is set to True. Then while running the orderUpdate over  the logs you can also be able to call the other calls too in the following manner 
	# print(fyers.get_profile())
	# print(fyers.tradebook())
	# print(fyers.positions())

	# fyersSocket.keep_running()
	
	  
def generate_fyers_model(app_id,access_token):
	#fyers = fyersModel.FyersModel(client_id=app_id, token=access_token,log_path="C:\\Users\\USERNAME\\Desktop\\Python\\FyersAPI")
	fyers = fyersModel.FyersModel(client_id=app_id, token=access_token,log_path=directory)
	print("Fyers models are now generated..")
	return fyers
	
def generate_fyers_socket(app_id,access_token):
	#fyersSocket = ws.FyersSocket(access_token=app_id+":"+access_token,run_background=False,log_path="C:\\Users\\USERNAME\\Desktop\\Python\\FyersAPI")
	fyersSocket = ws.FyersSocket(access_token=app_id+":"+access_token,run_background=False,log_path=directory)
	print("Fyers sockers are now generated..")
	return fyersSocket
	
def check_market_status(fyers):
	status=fyers.market_status()
	print(status)

	
'''
Symbol Master
You can get all the latest symbols of all the exchanges from the symbol master files

NSE – Currency Derivatives:
https://public.fyers.in/sym_details/NSE_CD.csv
NSE – Equity Derivatives:
https://public.fyers.in/sym_details/NSE_FO.csv
NSE – Capital Market:
https://public.fyers.in/sym_details/NSE_CM.csv
BSE – Capital Market:
https://public.fyers.in/sym_details/BSE_CM.csv
MCX - Commodity:
https://public.fyers.in/sym_details/MCX_COM.csv
'''


#Fetching Live Data
def generate_data_sets(session,access_token):
	#Generating fyers data model
	fyers=generate_fyers_model(session.client_id,access_token)
	
	#Generating fyers socket
	fyersSocket=generate_fyers_socket(session.client_id,access_token)
	
	#Check market status
	#check_market_status(fyers)
	
	#Fetching fyers Historical Data- Format 1
	#from_range=convert_mil_todate(current_milli_time(),'%Y-%m-%d')
	#to_range=convert_mil_todate(current_milli_time(),'%Y-%m-%d')
	#fetch_history_data_format1(fyers,"NSE:NIFTY50-INDEX","D",from_range,to_range)
	
	#Fetching fyers Historical Data- Format 2
	#from_range="1622097600"
	#to_range="1622097685"
	#fetch_history_data_format2(fyers,"NSE:NIFTY50-INDEX","D",from_range,to_range)
			
	#Fetching quotes data
	#fetch_quote_data(fyers,"NSE:NIFTY50-INDEX")
			
	#Fetching indepth data
	#fetch_indepth_data(fyers,"NSE:SBIN-EQ")
		
	#Fetching Live data with socket
	fetch_live_data(fyers,fyersSocket)
	
	
	
def main():
	#Fetching API Key last used, in firebase 
	auth_token=fetch_fyers_auth_token()
	if auth_token==None:
		print("No Token Found...")
	else:		
		auth_token=auth_token[api_child_name]
		print("Token found in the firebase...")
		#print(auth_token)
		
	#Initialise the fyers session
	session=initialise_fyers()
	if(session!=None):
		print("Checking auth key")
		access_token=check_auth_token(session,auth_token)
		
		if(access_token!=None):
			print("Generating acess token")
			#Generating access token
			access_code=session.generate_authcode()
			
			#Generate all the necessary datasets
			generate_data_sets(session,access_token)
			
	else:
		print("Something went wrong while initialisation.")
	

#Main program
if __name__ == '__main__':
	main()