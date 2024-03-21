import json
import helper_functions as help_functions


data=help_functions.readjson("toconvert.json")
print("Fetched data of ",len(data), " stocks")
fixeddata=help_functions.convert_nan_to_null(data)
help_functions.writejson("converted.json",fixeddata)