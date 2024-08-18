import nse_apis as nse_api
import pandas as pd

import grow_apis as grow_api

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

for stockname in stock_out:
	fin_id=stock_out[stockname]
	grow_api.get_icon_data(fin_id,stockname)
