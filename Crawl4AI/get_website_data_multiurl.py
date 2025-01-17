import os
import sys
import asyncio
from typing import List
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
import requests
import xml.etree.ElementTree as ET


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


async def crawl_parallel(urls: List[str], max_concurrent: int = 3):
    # Setup browser and crawler configuration
    browser_config = BrowserConfig(
        headless=True,
        extra_args=["--disable-gpu", "--disable-dev-shm-usage", "--no-sandbox"],
    )
    crawl_config = CrawlerRunConfig(cache_mode=CacheMode.BYPASS)

    # Create and start the crawler
    crawler = AsyncWebCrawler(config=browser_config)
    await crawler.start()

    try:
        success_count = 0
        fail_count = 0

        for i in range(0, len(urls), max_concurrent):
            batch = urls[i : i + max_concurrent]
            tasks = [crawler.arun(url=url, config=crawl_config) for url in batch]
            results = await asyncio.gather(*tasks, return_exceptions=True)

            for url, result in zip(batch, results):
                if isinstance(result, Exception):
                    print(f"Error crawling {url}: {result}")
                    fail_count += 1
                elif result.success:
                    success_count += 1
                else:
                    fail_count += 1

        print(f"\nSummary: {success_count} succeeded, {fail_count} failed")
    finally:
        await crawler.close()

async def main():
	sitemap_url = "https://paalana.in/page-sitemap.xml"
	urls = get_urls_from_sitemap(sitemap_url)
	await crawl_parallel(urls, max_concurrent=5)

if __name__ == "__main__":
    asyncio.run(main())
