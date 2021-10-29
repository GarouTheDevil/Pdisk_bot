import pymongo 
import os

DB_NAME = os.environ.get("DB_NAME", "devil")
DB_URL = os.environ.get("DB_URL", "mongodb+srv://devil1234:devil1234@cluster0.vcdhs.mongodb.net/devil?retryWrites=true&w=majority")
mongo = pymongo.MongoClient(DB_URL)
db = mongo[DB_NAME]
dbcol = db["pdisk"]

def insert(chat_id):
    user_id = int(chat_id)
    user_det = {
        "_id": user_id,
        "api_key": None
    }
    try:
        dbcol.insert_one(user_det)
    except Exception as e:
        print(e)

def find(chat_id):
    user_id = (chat_id)
    data = dbcol.find_one(
        {
            "_id": user_id
        }
    )
    api_key = data["api_key"]
    return api_key

def set(chat_id,api_key):
    dbcol.update_one(
        {
            "_id": chat_id
        },
        {
            "$set": 
                {
                    "api_key": api_key
                }
            }
    )

def getid():
    values = []
    for key in dbcol.find():
         id = key["_id"]
         values.append(id) 
    return values
