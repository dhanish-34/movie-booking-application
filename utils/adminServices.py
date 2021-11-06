from classes.movies import Movies
from utils.movie import addMovieDetailsToDB,deleteMovieDetailsFromDB

def adminOptions():
    print("\n\n1.Add Movies\n2.Remove Movies\n3.Exit")

def getMovieDetails():
    movie_name=input("\nEnter Movie name : ")
    movie_start_date=input("Enter Movie date in YYYY-MM-DD format: ")
    theatre_name=input("Enter Theatre name : ")
    ticket_price=input("Enter Ticket price : ")
    no_of_seats=int(input("Enter total number of seats : "))
    show_times = [str(show_time) for show_time in input("Enter the showtimes : ").split()]
    movieobject=Movies(movie_name,movie_start_date,theatre_name,ticket_price,show_times,no_of_seats)
    addMovieDetailsToDB(movieobject)
    print("\n\n------------------------------MOVIE ADDED SUCCESSFULLY-----------------------------")

def getRemoveMoviesDetails():
    movie_name=input("Enter Movie name : ")
    deleteMovieDetailsFromDB(movie_name)
    print("\n\n------------------------------MOVIE REMOVED SUCCESSFULLY-----------------------------")
