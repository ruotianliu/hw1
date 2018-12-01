import pymysql
import sys
import os


key = input("please input keyword: ")
db = pymysql.connect("localhost", "root", "lrtbest2018", "test")
myCursor = db.cursor()

#choose from table at label1
sql = "SELECT * FROM tweetsInfomation \
           WHERE labels LIKE '%s'" % (key)
myCursor.execute(sql)
Result = myCursor.fetchall()
for res in Result:
    print(res)
