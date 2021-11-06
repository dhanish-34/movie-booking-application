from utils.dbconnection import getConnection

def getListTheatre(movie_name):
    connection = getConnection()
    cursor = connection.cursor()
    cursor.execute("select * from theatre where movie_name='%s'"%movie_name)
    list=cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    return list

def getTheatreName(theatre_id):
    connection = getConnection()
    cursor = connection.cursor()
    cursor.execute("select theatre_name from theatre where theatre_id='%s'"%theatre_id)
    theatre=cursor.fetchone()
    connection.commit()
    cursor.close()
    connection.close()
    return theatre[0]