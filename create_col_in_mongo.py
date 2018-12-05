import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mongo_db = myclient["mongo_mini3"]
mongo_col = mongo_db['twitter']
