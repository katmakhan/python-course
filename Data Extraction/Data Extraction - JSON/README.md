# Fetching get request by setting User Agent parameter

### User Agent
The user agent is defined as "who" or "what" is requesting the page. It can be the following web browsers
	- Mozilla
	- Safari
	- Chrome
	
It can also be email readers. Some sites will have security features preventing automated web scrapping, by implementing a strict user agent rule, you can bypass that by setting the user agent field in the request parameter

### Bypass Cookies
- Initialise a `session`
- Visit the realpage to `set the cookies`
- Then request the json url with `user-agent` and `cookies` will be automatically added
- Bypassing the `session-cookies`

### Disclaimer
	- Please use this scripts for educational purpose only
	- Read the web scrapping policy of the website before scrapping it
	- You can be subjected to legal formalities when you violate their policies
	- Use web scraping for educational purpose only
	- Scrap with websites which do allow web scrapping