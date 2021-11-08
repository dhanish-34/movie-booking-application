from utils.movie import listMovies
from utils.theatre import getListTheatre,getTheatreName,filterByDate,filterByTheatre,filterByShowtime
from utils.showtimes import getListOfShowtimes,isTicketAvailable
from utils.bookings import createTicket,getAllBookingDetails,cancelTicketById
from utils.filter import displaybyDate,displayShowtime,displayByTheatre

def userOptions():
    print("\n\n1.List Movies\n2.Filter by Date/Showtime/Theatre\n3.Book Tickets\n4.Display Booking Details\n5.Cancel Ticket\n6.Exit\n")

def listMovieDetails():
    listMovies()

def bookingDetails(email):
    movie_name=input("Movie Name : ")
    listOfTheatres=getListTheatre(movie_name)
    print(listOfTheatres)
    print("\n",movie_name," SCREENING ON\n")
    print("\n\nTheatre ID    |    Theatre Name          |     TICKET PRICE")
    for i in listOfTheatres:
        print("------------------------------------------------------------------------\n")
        print(i[0],"                   ",i[1],"                   ",i[2],"\n")
    theatre_id=int(input("Enter Theatre ID :"))
    showtimes,ticket_price=getListOfShowtimes(theatre_id)
    print("\n\nSHOWTIME    |    AVAILABLE SEATS    ")
    for i in showtimes:
        print("-----------------------------------------\n")
        print(i[0],"                  ",i[1],"\n")
    show_time_input=input("\nEnter Showtime : ")
    number_of_seats=int(input("\nEnter number of seats : "))
    isvalid,available_tickets=isTicketAvailable(number_of_seats,showtimes,show_time_input)
    if(isvalid):
        total_amount=ticket_price*number_of_seats
        createTicket(movie_name,theatre_id,show_time_input,email,number_of_seats,total_amount,available_tickets)
        print("\n----------------------BOOKING SUCCESSFUL----------------------------------")
    elif(number_of_seats>available_tickets):
        print("Only ",available_tickets," is available")
    else:
        print("Only 10 ticketcan be booked per transaction")

def displayBookingDetails(email):
    listofbooking=getAllBookingDetails(email)
    for i in listofbooking:
        print(i[0],"     ",getTheatreName(i[2]),"        ",i[3],"         ",i[4],"        ",i[5],"        ",i[6])

def cancelTicket(email):
    listofbooking=getAllBookingDetails(email)
    for i in listofbooking:
        print(i[0],"   ",getTheatreName(i[2]),"        ",i[3],"         ",i[4],"        ",i[5],"        ",i[6])
    booking_id=int(input("Enter Booking ID for cancellation : "))
    cancelTicketById(booking_id,listofbooking)

def filterMovies():
    while(1):
        filterChoice=int(input("\n1.Filter on Date\n2.Filter on Theatre\n3.Filter on Showtime\n4.Exit\n\nEnter you choice : "))
        if(filterChoice==1):
            inputDate=input("Enter the date in YYYY-MM-DD format : ")
            listofmovies=filterByDate(inputDate)
            displaybyDate(listofmovies)
        elif(filterChoice==2):
            inputTheatre=input("Enter theatre name : ")
            listofmovies=filterByTheatre(inputTheatre)
            displayByTheatre(listofmovies)
        elif(filterChoice==3):
            inputShotime=input("Enter Showtime : ")
            listofmovies=filterByShowtime(inputShotime)
            displayShowtime(listofmovies)
        elif(filterChoice==4):
            break
        else:
            print("Invalid choice")