import json
import requests
from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Set up your API key using the value from .env
api_key_claude = os.getenv("ANTHROPIC_API_KEY")
api_key_chatgpt = os.getenv("CHATGPT_API_KEY")

# Initialize the Anthropic client with the API key
# anthropic = Anthropic(api_key=api_key)

# Your code continues here...
print(api_key)
