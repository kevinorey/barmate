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
        print("Leaving addRecordTODB")
   
def test():
    print("Entered liquor test")
    liquor = Liquor()
    liquor.addRecordToDB()
          
test()
