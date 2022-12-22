# Fetching last 30 days of Bhav data from NSE and analysing

### RUNNING Method
- Deleting any old files, to always keep last 30 days of data
- Fetching Bhav data from NSE, which is in ZIP file in 	`bhavfiles`
- Extact the csv files from all zip files and store to `csvbhav`
- Get the needed stocks from `resource` folder, and start analysis
- Calculate the `percentage change` and store day wise.
- Donot delete the `output.xlxs` as it contains the conditional formating to color `greeen` to all stocks above `1% change`


### NOTE
- Install all necessary dependencies
- Install `xlrd==1.2.0` because it only works with `xlxs` file.
- To uninstall xlrd and install the right version of xlrd.

```bash
pip uninstall xlrd
pip install xlrd==1.2.0
```


### Disclaimer
	- Please use this scripts for educational purpose only
	- Read the web scrapping policy of the website before scrapping it
	- You can be subjected to legal formalities when you violate their policies
	- Use web scraping for educational purpose only
	- Scrap with websites which do allow web scrapping