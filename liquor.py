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

        print("Getting db connection")
        connection = pymysql.connect(host="localhost", user="barmate", passwd="test1234", db="mydb")
        print("Successful db connection")
        
        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO `liquor` (`name`, `brand`, `abv`, `age`, `liquorType`) VALUES (%s, %s, %s, %s, %s)"
                print("Executing sql statement = " + sql)
                cursor.execute(sql, ('Jack Daniels', 'Gentleman Jack','45.6%', '12', 'Whiskey' ))
                print("Calling commit")
                connection.commit()
        except Exception as excep:
            print("Error occurred = ", excep)
                
        finally:
            print("Closing db connection....")
            connection.close()
        print("Leaving addRecordTODB")
   
def test():
    print("Entered liquor test")
    liquor = Liquor()
    liquor.addRecordToDB()
        
test()
