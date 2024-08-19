import nse_apis as nse_api
import pandas as pd
import os
import grow_apis as grow_api
import helper_functions as help_functions
# 16082024 NSE
# 20240816 BSE
df=nse_api.get_bse_bhav_data("20240816")
print(df)

stock_out={}
for index, row in df.iterrows():
	# Process each row
	# print(f"Index: {index}")
	symbol=row['TckrSymb']
	inst_id=row['FinInstrmId']
	stock_out[symbol]=inst_id


running_loc=help_functions.getscriptdir()
missing={}
for stockname in stock_out:
	fin_id=stock_out[stockname]
	icon_path=running_loc+"/Stock_Icons/"+stockname+".png"
	# print(icon_path)
	if os.path.exists(icon_path):
		# print("found for ",stockname)
		a=""
	else:
		if stockname[0].isalpha() and stockname[len(stockname)-1].isalpha():
			missing[stockname]=100
		else:
			# print("Maybe a invalid stockname ",stockname)
			a=""

print(missing)
