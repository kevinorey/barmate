import pymysql

class DBUtil():

    localHost = "localhost"
    user = "barmate"
    passwd = "test1234"
    db = "mydb"
    
    def __init__(self):
        print("Entered DBUtil constructor")

    def insert(self, sql, values):
        print("Entered insert")
        print("Input SQL = ", sql)
        print("Input values = ", values);

        print("Getting db connection")
        connection = pymysql.connect(host=self.localHost, user=self.user, passwd=self.passwd, db=self.db)
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


    def getAllRecords(self, sql, values):
        print("Entered get")
        print("Input SQL = ", sql)
        print("Input values = ", values);

        print("Getting db connection")
        connection = pymysql.connect(host=self.localHost, user=self.user, passwd=self.passwd, db=self.db)
        print("Successful db connection")
        
        try:
            with connection.cursor() as cursor:
               
                print("Executing sql statement = " + sql)
                cursor.execute(sql, values)
    
                results = cursor.fetchall()
                print(results)

                return results
        except Exception as excep:
            print("Error occurred = ", excep)
            raise Exception(excep)
                
        finally:
            print("Closing db connection....")
            connection.close()
        print("Leaving insert")
   

