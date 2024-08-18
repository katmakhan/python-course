import json
import requests

from dotenv import load_dotenv
import os

import nse_apis as nse_api
import helper_functions as help_function
from datetime import timedelta
import helper_charts as help_chart


import openai
# from openai import OpenAI

from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT

# Defining stockname globally
stockname="RELIANCE"
corporate_data=nse_api.get_corporate_info(stockname)
financial_data=corporate_data['financial_results']['data']
technical_data= help_function.readjson("Data/generated_values.json")
# chart_data=nse_api.get_intraday_chart_data(stockname)
# help_chart.create_chart_png(chart_data,stockname)


# # Load environment variables from .env file
# load_dotenv()

# # Set up your API key using the value from .env
# api_key_claude = os.getenv("ANTHROPIC_API_KEY")
# api_key_chatgpt = os.getenv("OPENAI_API_KEY")

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


# def call_chatgpt(prompt):
#     # Initialize the OpenAI client
#     client = OpenAI()  # Make sure you've set your API key in the environment variable

#     # Make a request to the ChatGPT API
#     response = client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {"role": "system", "content": "You are a financial analyst."},
#             {"role": "user", "content": prompt}
#         ],
#         max_tokens=1000
#     )

#     # Extract the generated content
#     generated_content = response.choices[0].message.content

#     # Print the generated content
#     print(generated_content)
#     return generated_content


# def call_claude(prompt):

# 	# Initialize the Anthropic client with the API key
# 	anthropic = Anthropic(api_key=api_key_claude)


# 	response = anthropic.completions.create(
# 		model="claude-2",
# 		max_tokens_to_sample=1000,
# 		prompt=f"{HUMAN_PROMPT} {prompt} {AI_PROMPT}",
# 	)

# 	blog_post = response.completion

# 	print(blog_post)
# 	return blog_post

def generate_blogpost():

	# Prepare the data for the prompt
	data_summary = f"""
	Technical Indicators:
	{json.dumps(technical_data["NSE:"+stockname+"-EQ"], indent=2)}

	Financial and Recent Announcements:
	{json.dumps(financial_data, indent=2)}
	"""

	# Prompt
	prompt = f"""
	You are a financial analyst specializing in technical analysis and stock market trends. 
	Using the provided data, create a concise blog post analysis for the stock NSE:20MICRONS-EQ.
	The blog post should include:

	1. Current Price
	1.1. If consecutive highs are breaking, or lows are breaking, about the pattern
	2. Technical Indicators (Action, Daily/Weekly/Monthly Strength)
	3. Key Technical Points
	4. Recent Corporate Actions
	5. Latest Announcements
	6. Analysis Summary
	7. Bullish Factors
	8. Cautionary Notes
	9. Support and Resistance levels
	10. Recommendations for different types of investors
	11. Risk Management advice

	Here's the data to use for your analysis:

	{data_summary}

	Please format the output as a concise, easy-to-read blog post. Do not include any disclaimers or mentions of AI in the output.
	"""

	messages=[
				{"role": "system", "content": "You are a financial analyst."},
				{"role": "user", "content": prompt}
			]

	print(messages)
	# call_chatgpt(prompt)
	# call_claude(prompt)


generate_blogpost()

