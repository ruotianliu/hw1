import pymongo
import sys
import os

key = input("please input label: ")
myclient = pymongo.MongoClient()
mydb = myclient.["mongo_mini3"]
    
myquery = {"label" : ("%s") % (key)}
data = mydb.twitterInfo.find(myquery)
for res in data:
    print(res)


