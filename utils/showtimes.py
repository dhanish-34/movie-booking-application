from utils.dbconnection import getConnection

def getListOfShowtimes(theatre_id):
    connection = getConnection()
    cursor = connection.cursor()
    cursor.execute("select s.show_time,s.available_seats from theatre t inner join show_timing s on t.theatre_id=s.theatre_id where t.theatre_id='%s'"%theatre_id)
    listofshowtimes=cursor.fetchall()
    cursor.execute("select ticket_price from theatre where theatre_id='%s'"%theatre_id)
    ticket_price=cursor.fetchone()
    connection.commit()
    cursor.close()
    connection.close()
    return listofshowtimes,ticket_price[0]

def isTicketAvailable(number_of_seats,showtimes,showtime_input):
    for i in showtimes:
        if(i[0]==showtime_input):
            available_seats=i[1]
            if(number_of_seats<=10 and number_of_seats<=i[1]):
                return 1,available_seats
    return 0,available_seats