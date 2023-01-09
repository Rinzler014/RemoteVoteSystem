from pymongo import MongoClient

# MONGO_URI = "mongodb://localhost:27017"

def get_db_handle(uri, db_name):

    client = MongoClient(uri)

    db = client[db_name]
                     
    return db