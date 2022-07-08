# Date Time Formats in Python

### Date and time Formats
- `%d`: Returns the date, from `1 to 31`
- `%m`: Returns the month, from `1 to 12`
- `%Y`: Returns the year in four-digit format like, `2021`
- `%y`: Reurns year in two-digit format like, `19, 20, 21`
- `%A`: Returns the weekday. Like, `Monday, Tuesday`
- `%a`: Returns the weekday (First three character.). Like, `Mon, Tue`
- `%B`: Returns the full name of the month like, `June, March`
- `%b`: Returns the short name of the month like, `Mar, Jun`
- `%H`: Returns the hour in 24-hours format `01 to 23`
- `%I`: Returns the hour in 12-hours format `01 to 12`
- `%M`: Returns the minute, from `00 to 59`
- `%S`: Returns the second, from `00 to 59`
- `%f`: Return the microseconds from `000000 to 999999`
- `%p`: Return time in `AM/PM` format
- `%c`: Returns a locale’s appropriate `date and time` representation
- `%x`: Returns a locale’s appropriate `date` representation
- `%X`: Returns a locale’s appropriate `time` representation
- `%z`: Return the `UTC offset` in the form ±HHMM[SS[.ffffff]]
- `%Z`: Return the `Time zone name` in the text form (Asia/Kolkotta)
- `%w`: Returns weekday as a decimal number, `where 0 is Sunday and 6 is Saturday`

### Sample code
```console
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
```