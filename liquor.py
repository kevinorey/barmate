import pymysql
import dbutil

class Liquor():

    age = None
    dateRecCreTs = None
    abv = None
    name = None
    liquorType = None
    brand = None
    
    def __init__(self):
        print("Entered Liquor constructor")

    def __init__(self, name, brand, abv, age, liquorType):
        self.name = name
        self.brand = brand
        self.abv = abv
        self.age = age
        self.liquorType = liquorType
        print("Entered Liquor constructor")

    def addRecordToDB(self):
        print("Entered addRecordToDB")
        print("Input Record =", self)
        
        try:
            db = dbutil.DBUtil()

            sql = "INSERT INTO `liquor` (`name`, `brand`, `abv`, `age`, `liquorType`) VALUES (%s, %s, %s, %s, %s)"
            values = (self.name, self.brand,self.abv, self.age, self.liquorType )

            print("Insert SQL = ", sql)
            print("Values = ", values)

            db.insert(sql, values)

        except Exception as excep:
            print("Error occurred = ", excep)
            raise Exception(excep)
                
        print("Leaving addRecordTODB")

    def getLiquorsFromDB(self):

        print("Entered getLiquorsFromDB")
        
        try:
            db = dbutil.DBUtil()

            results = db.getAllRecords("SELECT * FROM `liquor`", None)

            print("records fetched = ", results)

        except Exception as excep:
            print("Error occurred = ", excep)
            raise Exception(excep)
                
        print("Leaving addRecordTODB")
