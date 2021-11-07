from utils.dbconnection import getConnection

def createTicket(movie_name,theatre_id,show_time_input,email,number_of_seats,amount_paid,current_available_tickets):
    connection = getConnection()
    cursor = connection.cursor()
    print("MOVIE NAME        THEATRE ID        TIME            EMAIL       SEATS    PAID")
    print(movie_name,"               ",theatre_id,"          ",show_time_input,"        ",email,"       ",number_of_seats,"       ",amount_paid)
    cursor.execute("INSERT INTO bookings (email,theatre_id,movie_name,no_of_seats,show_time,amount_paid) VALUES (%s, %s, %s, %s, %s, %s)",(email,theatre_id,movie_name,number_of_seats,show_time_input,amount_paid))
    cursor.execute("UPDATE show_timing SET available_seats = %s WHERE theatre_id =%s and show_time=%s and movie_name=%s",(current_available_tickets-number_of_seats,theatre_id,show_time_input,movie_name))
    connection.commit()
    cursor.close()
    connection.close()

def getAllBookingDetails(email):
    connection = getConnection()
    cursor = connection.cursor()
    cursor.execute("select * from bookings where email='%s'"%email)
    listofbookedtickets=cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    return listofbookedtickets

def cancelTicketById(booking_id,list_of_booking):
    for i in list_of_booking:
        if(i[0]==booking_id):
            details=i
            break
    connection = getConnection()
    cursor = connection.cursor()
    cursor.execute("select available_seats from show_timing WHERE theatre_id =%s and show_time=%s and movie_name=%s",(details[2],details[5],details[3]))
    current_available_tickets=cursor.fetchone()
    print(current_available_tickets[0])
    cursor.execute("UPDATE show_timing SET available_seats = %s WHERE theatre_id =%s and show_time=%s and movie_name=%s",(int(current_available_tickets[0])+int(details[4]),details[2],details[5],details[3]))
    cursor.execute("delete from bookings where booking_id='%s'"%booking_id)
    connection.commit()
    cursor.close()
    connection.close()