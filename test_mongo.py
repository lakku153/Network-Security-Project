
from pymongo.mongo_client import MongoClient
from bson import SON

uri = "mongodb+srv://lokesh726888:Lokesh987@cluster0.oiqhv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)