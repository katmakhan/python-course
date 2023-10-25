import subprocess

# Data values to pass
api_key = "your_api_key"
user_id = "your_user_id"
uid = "your_uid"

# Call the shell script and pass data values as arguments
subprocess.call(["./shell_script.sh", api_key, user_id, uid])
