import mysql.connector
#from pydal import DAL, 
#from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
class UserDAO:
    
    #app = Flask(__name__, static_url_path='', static_folder='.')
    #app.config["DEBUG"] = True
    db=""
    def __init__(self): 
        self.db = mysql.connector.connect(
        host="http://MarionMcG.mysql.pythonanywhere-services.com",
        user="MarionMcG",
        password="Attymass",
        user="datarep",  # this is the user name on my mac
        passwd="password" # for my mac
        database="MarionMcG$users"
        )
    #SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
      #  username="MarionMcG",
     #   password="Attymass",
       # hostname="MarionMcG.mysql.pythonanywhere-services.com",
        #databasename="MarionMcG$users",
    #)
    #app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
    #app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
    #app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    #db = SQLAlchemy(app)
    #db = DAL('mysql://MarionMcG:Attymass@MarionMcG.mysql.pythonanywhere-services.com/MarionMcG$users')

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