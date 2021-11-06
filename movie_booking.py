from utils.dbconnection import getConnection
from utils.user import getUser
from classes.user import User
from utils.adminServices import adminOptions,getMovieDetails,getRemoveMoviesDetails
from utils.userServices import userOptions

email = input("Email :")
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