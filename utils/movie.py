from utils.dbconnection import getConnection

def addMovieDetailsToDB(movie):
    connection = getConnection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO movies (movie_name,movie_startdate) VALUES (%s, %s)",(movie.movie_name,movie.movie_start_date))
    cursor.execute("INSERT INTO theatre (theatre_name,ticket_price,movie_name) VALUES (%s, %s, %s)",(movie.theatre_name,movie.ticket_price,movie.movie_name))
    cursor.execute("select * from theatre where theatre_name='%s'"%movie.theatre_name)
    theatreobj = cursor.fetchone()
    booked_seats=0
    for showtime in movie.show_times:
        cursor.execute("INSERT INTO show_timing (theatre_id,movie_name,show_time,available_seats,booked_seats) VALUES (%s, %s, %s, %s, %s)",(int(theatreobj[0]),movie.movie_name,showtime,movie.no_of_tickets,booked_seats))
    connection.commit()
    cursor.close()
    connection.close()

def deleteMovieDetailsFromDB(movie_name):
    connection = getConnection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM show_timing WHERE movie_name='%s'"%movie_name)
    cursor.execute("DELETE FROM bookings WHERE movie_name='%s'"%movie_name)
    cursor.execute("DELETE FROM theatre WHERE movie_name='%s'"%movie_name)
    cursor.execute("DELETE FROM movies WHERE movie_name='%s'"%movie_name)
    connection.commit()
    cursor.close()
    connection.close()
