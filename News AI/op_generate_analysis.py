import nse_apis as nse_api
import helper_functions as help_function
import helper_charts as help_chart
import helper_analyser as help_analyse

import pandas as pd



# Defining stockname globally
stockname="RELIANCE"
corporate_data=nse_api.get_corporate_info(stockname)
financial_data=corporate_data['financial_results']['data']
technical_data= help_function.readjson("Data/generated_values.json")

chart_data=nse_api.get_intraday_chart_data(stockname)
help_function.writejson(f"Data/chart_{stockname}.json",chart_data)
help_chart.create_chart_png(chart_data,stockname)

top_10_near_52weekhigh=help_analyse.find_near_max_250_high(technical_data)
top_10_price_changer=help_analyse.create_top10_changes(technical_data)
top_10_volume_changer=help_analyse.create_top10_gainers_volume(technical_data)


help_chart.create_bargraph_png_icon(top_10_volume_changer,'volume_change_pct','Top 10 Stocks by Volume Change (Compared to 5-day SMA)','Volume Change (%)','Volume_graph',55,-100)
help_chart.create_bargraph_png_icon(top_10_price_changer,'price_change_pct','Top 10 Stocks by LTP Change (Compared to 10-day close)','Percent Change (%)','ltp_change_graph',12,-10)
help_chart.create_bargraph_png_icon(top_10_near_52weekhigh,"pcnt",'Top 10 Stocks by LTP Change (Compared to 52 week high)','Percent Change (%)','ltp_52weeknear_graph',2,2.5)