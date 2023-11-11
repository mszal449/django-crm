import mysql.connector

databse = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='password123'
)


# prepare a cursor object

cursorObject = databse.cursor()

# create a database

cursorObject.execute('Create database crmdb')

print('Database connected.')