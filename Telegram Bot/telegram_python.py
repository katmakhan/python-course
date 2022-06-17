import requests

#Bot Name: Btech_Trader
#If you don't have one, create one using botfather
#Create BOTS using https://t.me/botfather
#Put a unique profile pic for bot, for uniqueness
#Get the http api 
http_api="12345678-62d852hgWLhEc"

#Add the bot to the group
#Then go to this link to get the latest updates of the bot
#https://api.telegram.org/bot<http_api>/getUpdates
#Find the group id from updates "chat":{"id":-123456778"
chat_id="-123456778"


messageurl1="https://api.telegram.org/bot"+http_api+"/sendMessage?chat_id="+chat_id+"&text="

# Sent notification to telegram group
def update_telegram(title,body):
	msg1=messageurl1+title+"\n"+body
	requests.get(msg1)
	print("Sucesssfully sent the message")

update_telegram("Test","Test Message")