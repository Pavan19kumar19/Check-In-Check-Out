import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import NewRegisteration
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL' : "https://check-in-check-out-a0fbc-default-rtdb.firebaseio.com/"
})
ref = db.reference("Student")

data = NewRegisteration.data
#adding into the Realtime database
for key,value in data.items():
    ref.child(key).set(value)

print("Data uploaded Successfull...")