import pymysql
import dbutil

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
        
        try:
            db = dbutil.DBUtil()

            sql = "INSERT INTO `liquor` (`name`, `brand`, `abv`, `age`, `liquorType`) VALUES (%s, %s, %s, %s, %s)"
            values = ('Jack Daniels', 'Single Barrel','45.6%', '12', 'Whiskey' )

            db.insert(sql, values)

        except Exception as excep:
            print("Error occurred = ", excep)
                
        print("Leaving addRecordTODB")
   
def test():
    print("Entered liquor test")
    liquor = Liquor()
    liquor.addRecordToDB()
        
test()
