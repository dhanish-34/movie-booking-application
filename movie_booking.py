from utils.dbconnection import getConnection
from utils.user import getUser
from classes.user import User
from utils.adminServices import adminOptions,getMovieDetails,getRemoveMoviesDetails
from utils.userServices import userOptions,listMovieDetails,bookingDetails,displayBookingDetails,cancelTicket,filterMovies

email = input("\nEmail :")
user = getUser(email)

#Todo : add username
#Todo : move to user.py
if(user =='new'):
    role=input("Role (admin/user) : ")
    connection = getConnection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO user (email,role) VALUES (%s, %s)",(email.lower(),role.lower()))
    connection.commit()
    cursor.close()
    connection.close()
    user = User(getUser(email))
else:
    user = User(user)

if(user.role=="admin"):
    while(1):
        adminOptions()
        option=int(input("Enter Option :"))
        if(option==1):
            getMovieDetails()
        elif(option==2):
            getRemoveMoviesDetails()
        elif(option==3):
            break
        else:
            print("Invalid Option")
elif(user.role=="user"):
    while(1):
        userOptions()
        option=int(input("Enter Option :"))
        if(option==1):
            listMovieDetails()
        elif(option==2):
            filterMovies()
        elif(option==3):
            bookingDetails(email)
        elif(option==4):
            displayBookingDetails(email)
        elif(option==5):
            cancelTicket(email)
        elif(option==6):
            break
        else:
            print("Invalid Option")