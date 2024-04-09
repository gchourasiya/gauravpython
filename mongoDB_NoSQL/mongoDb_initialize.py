import pymongo as pym
import dns
dbinput = "mongodb+srv://gchourasiya:tMR_B6EdRNWgwyt@cluster0.mw4lg.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
connection = pym.MongoClient(dbinput)
# mydb = client["mydatabase"]
# mycol = mydb["customers"]

print(connection.list_database_names())

import pymongo as pym
# connection = pym.MongoClient("<the atlas connection string>")
test_db = connection.data
collection = test_db.test_coll
query = {'sec': 'A'}
new_update = {'$set': {'sec': 'C'}}
updated = collection.update_many(query, new_update)
cursor = collection.find({})
def sliceDict(dict1:dict):
  new_dict = {key:value for key,value in dict1.items() if not key.startswith('_id')}
  return new_dict
for document in cursor:
  doc = sliceDict(document)
  print(doc)
mylist = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "name": "Ben", "address": "Park Lane 38"},
  { "name": "William", "address": "Central st 954"},
  { "name": "Chuck", "address": "Main Road 989"},
  { "name": "Viola", "address": "Sideway 1633"}
]