import pymysql

class Liquor():

    age = None
    dateRecCreTs = None
    abv = None
    name = None
    liquorType = None
    brand = None
    name = None
    
    def __init__(self):
        print("Entered Liquor constructor")

    def addRecordToDB(self):
        print("Entered addRecordToDB")
        print("Input Record =", self)
        
        #cnx = connection.MySQLConnection(user='barmate', password='test123',host='127.0.1.1',database='mydb')
        #cnx.close()
        # Open database connection
        #db = pymysql.connect("127.0.1.1","barmate","test1234","mydb" )
        db = pymysql.connect(host="localhost", user="barmate", passwd="test1234", db="mydb")
        db.close()
        print("Leaving addRecordTODB")
   
def test():
    print("Entered liquor test")
    liquor = Liquor()
    liquor.addRecordToDB()
        
test()
