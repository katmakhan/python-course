# Fetching Fyers APP data


### GET URL
- To view all apps
```url
https://api-t1.fyers.in/api/v2/user/user-apps
```

### PUT PAYLOADS
- TO create a new app
- Request
```json
{
  "appName": "LoginTest",
  "description": "This is generated via api calls,",
  "permissions": [
    "x:0",
    "x:1",
    "x:2",
    "d:1",
    "d:2"
  ],
  "redirectUrl": "https://trade.fyers.in/api-login/redirect-uri/index.html",
  "webhook": [],
  "image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAZAAAAGQCAYAAACAvzbMAAAABmJLR0QA/wD/AP+gvaeTAACBPklEQVR42ux9CZhV1ZVumU530un33ve9Tk9Jp7t"
}
```
- Sucessfull is code `2201` with json
- Response
```json
{
  "code": 2201,
  "message": "App created successfully. Your App Id is XXXXX-100 and App Secret is XXXX.",
  "s": "ok"
}
```

### Regenerate Secrets
```json
{
  "appId": "XXXX-100",
  "appName": "LoginTest",
  "description": "This is generated via api calls.",
  "generatePassword": true,
  "image": null,
  "img_delete": false,
  "redirectUrl": "https://trade.fyers.in/api-login/redirect-uri/index.html",
  "webhook": []
}

```

### DELETE PAYLOAD
```json
{
  "appId": "P21EZW8UMN-100"
}
```
### Disclaimer
	- Please use this scripts for educational purpose only
	- Read the web scrapping policy of the website before scrapping it
	- You can be subjected to legal formalities when you violate their policies
	- Use web scraping for educational purpose only
	- Scrap with websites which do allow web scrapping