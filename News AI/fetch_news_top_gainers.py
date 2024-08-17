import json
import requests
from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT
from dotenv import load_dotenv
import os
import nse_apis as nse_api
import helper_functions as help_function
from datetime import timedelta
import helper_charts as help_chart

# Defining stockname globally
stockname="RELIANCE"
# corporate_data=nse_api.get_corporate_info(stockname)
# financial_data=corporate_data['financial_results']['data']
# technical_data= help_function.readjson("Data/generated_values.json")

def get_historical():
	# Getting Historical Data
	# 18-04-2024
	to_date_obj=help_function.today()
	from_date_obj=help_function.today()-timedelta(days=365)


	to_date_str=help_function.convert_to_date_str(to_date_obj,"%d-%m-%Y")
	from_date_str=help_function.convert_to_date_str(from_date_obj,"%d-%m-%Y")

	# Get historical data of 365 days
	hist_data=nse_api.get_historical_data(stockname,from_date_str,to_date_str)
	return hist_data


# # Load environment variables from .env file
# load_dotenv()

# # Set up your API key using the value from .env
# api_key_claude = os.getenv("ANTHROPIC_API_KEY")
# api_key_chatgpt = os.getenv("CHATGPT_API_KEY")

# # Initialize the Anthropic client with the API key
# anthropic = Anthropic(api_key=api_key_claude)


# # Prepare the data for the prompt
# data_summary = f"""
# Technical Indicators:
# {json.dumps(technical_data["NSE:"+stockname+"-EQ"], indent=2)}

# Financial and Recent Announcements:
# {json.dumps(financial_data, indent=2)}
# """



chart_data=nse_api.get_intraday_chart_data(stockname)

help_chart.create_chart_png(chart_data,stockname)
