### To find users in a wordpress site
```
/wp-json/wp/v2/users/1
```
```
/?author=1 
```
### To protect
- Add security rule in cloudflare.
```
(http.request.full_uri contains "/wp-json")
```
[Refference](https://www.wp-tweaks.com/hackers-can-find-your-wordpress-username/)

### Disclaimer
	- Please use this scripts for educational purpose only
	- Read the web scrapping policy of the website before scrapping it
	- You can be subjected to legal formalities when you violate their policies
	- Use web scraping for educational purpose only
	- Scrap with websites which do allow web scrapping