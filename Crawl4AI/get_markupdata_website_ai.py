import asyncio
from crawl4ai import *
import xml.etree.ElementTree as ET
import requests
from urllib.parse import urlparse


def get_urls_from_sitemap(sitemap_url: str):
	try:
		# Fetch the sitemap content
		response = requests.get(sitemap_url)
		response.raise_for_status()  # Raise an error for bad status codes

		# Parse the XML content
		root = ET.fromstring(response.content)

		# Extract URLs
		urls = [element.text for element in root.iter("{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]
		
		return urls

	except requests.RequestException as e:
		print(f"Error fetching the sitemap: {e}")
	except ET.ParseError as e:
		print(f"Error parsing the XML: {e}")


async def save_markdown_content(url: str, file_path: str):
	async with AsyncWebCrawler() as crawler:
		result = await crawler.arun(url=url)
		
		# Save the markdown content to a file
		with open(file_path, "w", encoding="utf-8") as file:
			file.write(result.markdown)
	
	print(f"Markdown content saved to {file_path}")

async def main():
	url = "https://www.paalana.in"
	file_path = "result.md"
	
	# Save the markdown content
	# await save_markdown_content(url, file_path)
	
	# Call the function to process the menu items
	sitemap_url = "https://paalana.in/page-sitemap.xml"
	url_list = get_urls_from_sitemap(sitemap_url)

	if url_list:
		print("List of URLs from sitemap:")
		for url in url_list:
			print(url)
			title=urlparse(url).path.strip("/")
			print(title)
			await save_markdown_content(url,"./InsidePages/" +title+".md")

if __name__ == "__main__":
	asyncio.run(main())
