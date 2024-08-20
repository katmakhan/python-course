import nse_apis as nse_api
import helper_functions as help_function
import helper_charts as help_chart
import helper_analyser as help_analyse

import pandas as pd



def generate_chart_data(stockname,chart_data):
	chart_data=nse_api.get_intraday_chart_data(stockname)
	help_function.writejson(f"Data/chart_{stockname}.json",chart_data)
	help_chart.create_chart_png(chart_data,stockname)


def generate_analysis(technical_data,which,scale_val):
	top_10_near_52weekhigh=help_analyse.find_near_max_250_high(technical_data)
	top_10_price_changer=help_analyse.create_top10_changes(technical_data)
	top_10_volume_changer=help_analyse.create_top10_gainers_volume(technical_data)


	help_chart.create_bargraph_png_icon(top_10_volume_changer,'volume_change_pct','Top 10 Stocks by Volume Change (Compared to 5-day SMA)','Volume Change (%)',f'Volume_graph_{which}',55,-100)
	help_chart.create_bargraph_png_icon(top_10_price_changer,'price_change_pct','Top 10 Stocks by LTP Change (Compared to 10-day close)','Percent Change (%)',f'ltp_change_graph_{which}',12,-10)
	help_chart.create_bargraph_png_icon(top_10_near_52weekhigh,"pcnt",'Top 10 Stocks by LTP Change (Compared to 52 week high)','Percent Change (%)',f'ltp_52weeknear_graph_{which}',2,2.5)

def main():
	#Loading nifty 50 and nifty 200 stocks
	nifty50_stocks=help_function.readjson("Data/NIFTY50_Stocks.json")
	nifty200_stocks=help_function.readjson("Data/NIFTY200_Stocks.json")

	# Defining stockname globally
	stockname="RELIANCE"
	# corporate_data=nse_api.get_corporate_info(stockname)
	# financial_data=corporate_data['financial_results']['data']
	technical_data= help_function.readjson("Data/generated_values.json")

	filtered_data_nifty50 = {key: value for key, value in technical_data.items() if key in nifty50_stocks}
	filtered_data_nifty200 = {key: value for key, value in technical_data.items() if key in nifty200_stocks}

	# generate_chart_data(stockname,financial_data)
	# generate_analysis(technical_data,"total",1)
	# generate_analysis(filtered_data_nifty50,"nifty50",0.3)
	# generate_analysis(filtered_data_nifty200,"nifty200",0.4)

	# Filter the DataFrame to only include the selected columns
	help_chart.create_heatmap(filtered_data_nifty50,"heatmap_nifty50")
	help_chart.create_heatmap(filtered_data_nifty200,"heatmap_nifty200")
	help_chart.create_heatmap(technical_data,"heatmap_total")


main()
