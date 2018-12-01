import pymysql

# connect to the database
db = pymysql.connect("localhost", "root", "lrtbest2018", "test")

myCursor = db.cursor()

#create a table called tweetsInfo to store name, #of images, labels
myCursor.execute("CREATE TABLE tweetsInfomation (name VARCHAR(255), image_id INTEGER(10), image_num INTEGER(10), label VARCHAR(255))")
