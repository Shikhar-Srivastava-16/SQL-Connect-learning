"""
Used to create a database on mySQL
"""

import mysql.connector as m

"""
used to add records to table, only caters to the table in databaseMain.py 
"""
def insertRecord(cursorName):
    while (True):
        #ask for entry 
        ask = input("Do you want to enter more details? (yes/no)")
        if ask.lower().strip() == "no":
            break

        name = input("Enter Student full name: ")
        rollno = input("Enter 10 digit roll number: ")
        subject = input("Enter Student's subject of study: ")
        execStr = 'insert into students values ("'+name+'", "'+rollno+'", "'+subject+'");'
        cursorName.execute(execStr)

"""
Used to add a value to specific field
"""
def insertValue(cursorName, fieldToUse):
    value = input("Enter value to insert: ")
    execStr = 'insert into students ('+fieldToUse+') values ("'+value+'");'
    cursorName.execute(execStr)

'''
more functions can be added and used to databaseMain
'''