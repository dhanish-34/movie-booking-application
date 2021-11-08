def displaybyDate(listByDate):
    print("\nDATE             THEATREID       PRICE         THEATRE              MOVIE")
    for i in listByDate:
        print("\n",i[1],"        ",i[2],"        ",i[4],"        ",i[3],"         ",i[0])

def displayByTheatre(listByDate):
    print("\nDATE             THEATREID       THEATRE      PRICE       MOVIE")
    for i in listByDate:
        print("\n",i[1],"        ",i[2],"        ",i[3],"        ",i[4],"      ",i[0])

def displayShowtime(listofmovies):
    print("\nSHOWTIME   AVAILABLE SEATS      TICKET PRICE      THEATRE         MOVIE")
    for i in listofmovies:
        print("\n",i[2],"        ",i[3],"                ",i[8],"           ",i[7],"         ",i[1])