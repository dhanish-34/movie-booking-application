from utils.dbconnection import getConnection
# display products
def getUser(email):
    connection = getConnection()
    cursor = connection.cursor()
    cursor.execute("select * from user where email='%s'"%email)
    user = cursor.fetchone()
    connection.commit()
    cursor.close()
    connection.close()
    if(user):
        return user
    return 'new'
    # return user