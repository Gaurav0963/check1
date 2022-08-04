import pymongo
client = pymongo.MongoClient("mongodb+srv://Gaurav:mongodb@gaurav.dxwsk.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d ={
    'name' : 'Gaurav',
    'lastname' : 'Rajput',
    'email':'gsr094@gmail.com'
}

db1 = client['file1']
coll = db1['test']
coll.insert_one(d)