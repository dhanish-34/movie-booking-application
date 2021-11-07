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

def filterByDate(inputDate):
    connection = getConnection()
    cursor = connection.cursor()
    cursor.execute("select * from movies m inner join theatre t where m.movie_name=t.movie_name and m.movie_startdate<'%s'"%inputDate)
    list=cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    return list

def filterByTheatre(theatre_name):
    connection = getConnection()
    cursor = connection.cursor()
    cursor.execute("select * from movies m inner join theatre t where m.movie_name=t.movie_name and t.theatre_name='%s'"%theatre_name)
    list=cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    return list

def filterByShowtime(showtime):
    connection = getConnection()
    cursor = connection.cursor()
    cursor.execute("select * from show_timing s inner join theatre t where s.theatre_id=t.theatre_id and s.show_time='%s'"%showtime)
    list=cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    return list
