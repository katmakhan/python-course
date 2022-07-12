# Parse the CSV file hosted in a public domain

https://public.fyers.in/sym_details/NSE_FO.csv

### Sample code for fetching csv file for stock information from fyers
```python
#Import Functions
import csv
import pandas as pd

# Get data Function
def getexpirydata(site):
	print("Reading from site..")
	dataframe = pd.read_csv(site,header=None)
	#pd.close()
	
	#print(df)
	print("\n")
	cr=csv.reader(dataframe)
	
	count =0
	total_list=[]
	total_list_stocks=[]
	for index, row in dataframe.iterrows():
		option=row[1]
		#print(option)
		count=count+1
		
	print("Completed fetching ",count," files")

#Main Program
site="https://public.fyers.in/sym_details/NSE_FO.csv"		
getexpirydata(site)

```