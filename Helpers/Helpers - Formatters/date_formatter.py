from datetime import datetime

#Convert date object to date string
def convert_to_date_obj(date_str,date_format):
	date_obj = datetime. strptime(date_str,date_format)
	return date_obj

#Convert date string into date object
def convert_to_date_str(date_obj,date_format):
	date_str=date_obj.strftime(date_format)
	return date_str

#Main Function
#Assign sample date in string
date_str="12-Aug-2012"
date_format="%d-%b-%Y"

#Date string and format should be same, else it will throw an error
date_obj=convert_to_date_obj(date_str,date_format)
print("Date Object is: ",date_obj)

# Get current Date in date Object
#date_obj = datetime.now()
date_format="%d %B %y %H:%M:%S"
#print('Current Date:', date_obj)

date_str=convert_to_date_str(date_obj,date_format)
print("Date String is: ",date_str)