from datetime import datetime
from datetime import timedelta

#Convert date string into date object
def convert_to_date_str(date_obj,date_format):
	date_str=date_obj.strftime(date_format)
	return date_str

prev_day=datetime.now() - timedelta(days=1)
prev_day_str=convert_to_date_str(prev_day,"%d-%b-%y")
print(prev_day_str)