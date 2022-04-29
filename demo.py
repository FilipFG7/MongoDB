import pymongo


# connect
connectstring = "mongodb+srv://FilipFG7:password@cluster0.a2cuc.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
myclient = pymongo.MongoClient(connectstring, tls=True, tlsAllowInvalidCertificates=True)


# create
mydb = myclient["mydatabase"]
mycol = mydb["customers"]


# create a new document
#mycol.insert_one({".id":101, "companyname":"Kea", "contact":"Filip Gavalier"})
#mycol.insert_one({".id":102, "companyname":"CBA", "contact":"Cristiano Ronaldo"})
#mycol.insert_one({".id":103, "companyname":"CBS", "contact":"Karim Benzema"})


# exclude id and lastname
#for x in mycol.find({}, { "-id": 0, "companyname": 0}):
#    print(x)


# update one - only first one
#myquery = { "companyname": "Kea" }
#newvalues = { "$set": { "companyname": "New Kea" } }
#mycol.update_one(myquery, newvalues)