# Fyers API Connection Using Telegram and Firebase Database Updation
This will be a lengthy and complicated query, where the logic is to fetch the stock details and api key stored in firebase database.

- Fetching the API Key from Firebase Database
	Storing the API Keys in cloud Database for further expansion (Store in Encrypted form)
- Sending New API Request via Telegram
	Send the link to re initalise the api , as fyers api have a reset time of 24hrs. This is for security purpose
- Fetching List of Stock Names and Options
	Get the name and add extra bit of informations so that the fyers api can subscribe to live data for the specified stocks or option chain
- Storing It temporarly for BULK Update, rather than 1 second Update
	Updating in realtime in firebase will be a huge over head cost
	- Updating 100+ stocks in realtime in each child node is extensive
	- Realtime upadtion of 20 symbols will have 20-30mb usage
	- Updating the whole 20 symbols in a single strech will be 3-4 mb
	- We can reduce the usage further by storing only the signficant digits rather than whole millisecond
	- This will also introduce a optimisation of 50%
	- Initially you can try updating in realtime
	- Then gradually implement the optimisation method for production level
	
- Integration all the above unit functions
	- Integrate all the above functionality into one single python
	- Upload the same into HEROKU for cloud execution
	- Make sure that you turn on the dyno only during market hours
	- Its also good practise to use webhook for api call backs
	- That will be discussed in firebase integration (Firebase cloud functions)

### Fetching the API Key from Firebase Database


### Sending New API Request via Telegram


### Fetching List of Stock Names and Options

### Storing It temporarly for BULK Update, rather than 1 second Update

### Integration all the above unit functions