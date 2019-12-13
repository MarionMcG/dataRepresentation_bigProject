import pymysql
class userDAO:
    db=""
    

    def __init__(self): 
        self.db = pymysql.connect(host = "localhost", 
                            user = "root", 
                            password="root", 
                            db = "users", 
                            cursorclass = pymysql.cursors.DictCursor)
    #Creating a new user adds data to both tables                        
      
    def create(self, values):
        cursor = self.db.cursor()
        sql="insert into  user_info  ( user ,  email ,  edits ,  permission ) values (%s,%s,0,'Editor')"
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid

    def getAll(self):
        cursor = self.db.cursor()
        sql="select * from user_info"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        print(results)
        for result in results:
            print(result)
            returnArray.append(result)
        return returnArray

    def findByID(self, id):
        cursor = self.db.cursor()
        sql="select * from user_info where id = %s" 
        values = (id,)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return result

    def update(self, values):
        cursor = self.db.cursor()
        sql="update  user_info  set  user = %s,  email =%s,  edits =%s,  permission =%s where  id  = %s" 
        cursor.execute(sql, values)
        self.db.commit()
    
    def delete(self, id):
        cursor = self.db.cursor()
        sql="delete from  user_info  where  id = %s"
        values = (id,)
        cursor.execute(sql, values)
        self.db.commit()
        print("delete done") 


UserDAO = userDAO()