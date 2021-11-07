def display(listByDate):
    for i in listByDate:
        print("\n",i[0],"        ",i[1],"      ",i[2],"        ",i[3],"    ",i[4])

def displayShowtime(listofmovies):
    print("SHOWTIME   AVAILABLE SEATS      TICKET PRICE      THEATRE         MOVIE")
    for i in listofmovies:
        print("\n",i[2],"        ",i[3],"         ",i[8],"           ",i[7],"         ",i[1])
