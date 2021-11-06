import mysql.connector
def getConnection():
    connection = mysql.connector.connect(host="localhost", user="root",password="root",database='movie_booking')
    return connection