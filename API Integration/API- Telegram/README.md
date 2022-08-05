# Bot Name: Btech_Trader
- If you don't have one, create one using botfather
- Create BOTS using https://t.me/botfather
- Put a unique profile pic for bot, for uniqueness
- Get the http api key, and save it securely

### Sample http_api key
```console
http_api="123456789:HKSDFKFSLSFHFSJKS-6r4L5hgWLhEc"
```

### Getting the chatid of the GROUP
- Add the bot to the group
- Then go to this link to get the latest updates of the bot
  ```console
  https://api.telegram.org/bot<http_api>/getUpdates
  ```
  ```console
  https://api.telegram.org/bot123456789:HKSDFKFSLSFHFSJKS-6r4L5hgWLhEc/getUpdates
  ```
- Find the group id from updates "chat":{"id":-123456"

# Sample Chat ID
```console
chat_id="-123456"
```

### KEYPOINTS
- WHEN YOU CHANGE THE ADMIN RIGHTS OF THE BOT TO READ MESSSAGE TO RECEIVE UPDATES
  - Make sure you change the channel ID, cause once you change the permissions of the bot, the channel id becomes different

- WHEN you send special characters like "&", telegram won't send the msg, so you need to parse them via urllib
