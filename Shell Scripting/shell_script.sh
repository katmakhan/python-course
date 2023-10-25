#!/bin/bash

# Receive APIKEY, USERID, and UID as command-line arguments
api_key="$1"
user_id="$2"
uid="$3"

# Call the inner Python script and pass the data values as arguments
python3 python_script_2.py "$api_key" "$user_id" "$uid"
