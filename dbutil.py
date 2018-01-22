import pymysql

class DBUtil():
    
    def __init__(self):
        print("Entered DBUtil constructor")

    def insert(self, sql, values):
        print("Entered insert")
        print("Input SQL = ", sql)
        print("Input SQL = ", values);

        print("Getting db connection")
        connection = pymysql.connect(host="localhost", user="barmate", passwd="test1234", db="mydb")
        print("Successful db connection")
        
        try:
            with connection.cursor() as cursor:
               
                print("Executing sql statement = " + sql)
                cursor.execute(sql, values)
                print("Calling commit")
                connection.commit()
        except Exception as excep:
            print("Error occurred = ", excep)
            raise Exception(excep)
                
        finally:
            print("Closing db connection....")
            connection.close()
        print("Leaving insert")
   

