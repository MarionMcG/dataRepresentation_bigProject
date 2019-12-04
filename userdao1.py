import mysql.connector

class UserDAO:
    db=""
    def __init__(self): 
        self.db = mysql.connector.connect(
        host="http://MarionMcG.mysql.pythonanywhere-services.com",
        user="MarionMcG",
        password="Attymass",
        #user="datarep",  # this is the user name on my mac
        #passwd="password" # for my mac
        database="MarionMcG$users"
        )
    
            
    def create(self, values):
        cursor = self.db.cursor()
        sql="insert into user_info (user, email, edits, permission) values (%s,%s, 0, 'Editor')"
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
            returnArray.append(self.convertToDictionary(result))

        return returnArray

    def findByID(self, id):
        cursor = self.db.cursor()
        sql="select * from user_info where id = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDictionary(result)

    def update(self, values):
        cursor = self.db.cursor()
        sql="update user_info set name= %s, age=%s  where id = %s"
        cursor.execute(sql, values)
        self.db.commit()
    def delete(self, id):
        cursor = self.db.cursor()
        sql="delete from user_info where id = %s"
        values = (id,)

        cursor.execute(sql, values)

        self.db.commit()
        print("delete done")

    def convertToDictionary(self, result):
        colnames=['id','user','email', 'edits', 'permission']
        item = {}
        
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
        
        return item
    


userDAO = UserDAO()