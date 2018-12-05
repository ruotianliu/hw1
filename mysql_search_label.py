import pymysql
import sys
import os


key = input("please input label: ")
db = pymysql.connect("localhost", "root", "lrtbest2018", "test")
myCursor = db.cursor()

sql = "SELECT * FROM tweetsInfomation \
           WHERE labels LIKE '%s'" % (key)
myCursor.execute(sql)
Result = myCursor.fetchall()
for res in Result:
    print(res)
