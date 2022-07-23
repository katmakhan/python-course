# python-free-course
Learn python and the basics of most of the production level architecture using python as backend. Functions like database READ WRITE DELETE operations, deployment in cloud platforms like gcloud and heroku for better automation of your work.

- [Async Functions](https://github.com/katmakhan/python-course/tree/master/Functions/Functions%20-%20Asyncio)
- [Formating Date and Time](https://github.com/katmakhan/python-course/tree/master/Helpers/Helpers%20-%20Formatters)
- [Creating Telegram Bots](https://github.com/katmakhan/python-course/tree/master/API%20Integration/API-%20Telegram)
- Webscraping and parsing of json/ csv files
- Cloud functions and deployment

### CMD from opened folder in WINDOWS
press `Alt` + `D` then type `cmd`

### Testing the python using online compiler
https://www.programiz.com/python-programming/online-compiler/

### Below are the character codes to format the date and time

- `%d`: Returns the date, from `01 to 31`
- `%m`: Returns the month, from `01 to 12`
- `%#m`: Returns the month, from `1 to 12` without starting 0 in Windows Only
- `%-m`: Returns the month, from `1 to 12` without starting 0 in mac/Unix/Linux
- `%Y`: Returns the year in four-digit format like, `2021`
- `%y`: Reurns year in two-digit format like, `19, 20, 21`
- `%A`: Returns the weekday. Like, `Monday, Tuesday`
- `%a`: Returns the weekday (First three character.). Like, `Mon, Tue`
- `%B`: Returns the full name of the month like, `June, March`
- `%b`: Returns the short name of the month like, `Mar, Jun`
- `%H`: Returns the hour in 24-hours format `01 to 23`
- `%I`: Returns the hour in 12-hours format `01 to 12`
- `%M`: Returns the minute, from `00 to 59`
- `%S`: Returns the second, from `00 to 59`
- `%f`: Return the microseconds from `000000 to 999999`
- `%p`: Return time in `AM/PM` format
- `%c`: Returns a locale’s appropriate `date and time` representation
- `%x`: Returns a locale’s appropriate `date` representation
- `%X`: Returns a locale’s appropriate `time` representation
- `%z`: Return the `UTC offset` in the form ±HHMM[SS[.ffffff]]
- `%Z`: Return the `Time zone name` in the text form (Asia/Kolkotta)
- `%w`: Returns weekday as a decimal number, `where 0 is Sunday and 6 is Saturday`


### Sample code for iterating through the `Dictionary/Json`
```python
test_dict = {}
test_dict={'name1':'akku','name2':'basi','name3':'pheeby','name4':'achumon'}

for key in test_dict:
	print("Key is ",key)
	print("Value is ",test_dict[key])
	print("________________")
```

### Sample code for iterating through the `Array`
```python
test_array = []
test_array=['akku','basi','pheeby']

for name in test_array:
	print("Name is ",name)
	print("________________")
```

### Getting first key `without iterating` through the `dictionary`
```python
first_key=next(iter(test_dict))
```
### Example
```python
test_dict = {'key1' : 'value 1', 'key2' : 'value 2', 'key3' : 'value 3'}
first_key = next(iter(test_dict))
first_value=test_dict[first_key]

print("First key is: ",first_key)
print("First Value is: ",first_value)
```


### Sample code to merge two dictionary
```python

def combine_dict(dict1,dict2):
	dict={}
	
	for key in dict1:
		#If there is no key inside combined_cepe
		#Add the data
		if dict.get(key) is None:
			dict[key]=dict1[key]
		else:
			print("Already there is key in dict 1")
			
	for key in dict2:
		#If there is no key inside combined_cepe
		#Add the data
		if dict.get(key) is None:
			dict[key]=dict2[key]
		else:
			print("Already there is key in dict 2")
			
	#Return the combined dict
	return dict
```

