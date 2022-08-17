### Firebase Imports Functions

```python
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
```

### Initialising admin sdk
```python
cred = credentials.Certificate("./firebase-admin-key.json")
print("initilising firebase app")

#Initilising Database
firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://<project-id>-<database-instance>.firebaseio.com/'
})

# Initilising Database 2
app2 = firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://<project-id>-<database-instance>.firebaseio.com/'
}, name='app2')
```
### Fetch Data from firebase
```python
def fetch_data_firebase(path):
	ref=db.reference('Users',app2).child(path)
	data=ref.get()
	print(data)
	print("Succesfully fetched data from firebase ")
```

### Update Data from firebase
```python
def update_data_firebase(path,data):
	ref=db.reference('Users',app2).child(path)
	ref.set(data)
	print("Succesfully updated the data in firebase")
```

### Delete Data from firebase
```python
def delete_data_firebase(path):
	ref=db.reference('Users',app2).child(path)
	ref.delete()
	print("Succesfully deleted the data from firebase")
```

### Sample Main Function
```python
def main():
	fetch_data_firebase("Registered")

	data_to_update={"my-key": "value"}
	update_data_firebase("Updated",data_to_update)

	delete_data_firebase("UnRegistered")

#Main program
if __name__ == '__main__':
	main()
```
