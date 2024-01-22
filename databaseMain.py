import mysql.connector as m
import databaseLib as lib
#Opening database
mydb = m.connect(
    host = "localhost",
    user = "root",
    password = "myPass_Shikhar",
    database = "practice"
)

myCursor = mydb.cursor()

myCursor.execute("CREATE TABLE students (name varchar(50), rollno varchar(10), subject varchar(50));")
lib.insertRecord(myCursor)
myCursor.close()
