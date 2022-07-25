from datetime import datetime
from datetime import timedelta

curr_day=datetime.now()
curr_day.replace(hour=7,minute=30)
seconds=round(curr_day.timestamp())

print("Current date in seconds",seconds)