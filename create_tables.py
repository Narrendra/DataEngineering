#This file creates the tables in SQL SERVER
# import pyodbc
import pyodbc

#Create a connection with MS SQL SERVER 

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-DC1BM20;'
                      'Database=master;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT * FROM student')

for row in cursor:
    print(row)

# def checkIfDBExists(dbName)

