import mysql.connector as connector
class DV:
        def __init__(self):
            self.con = connector.connect(host='localhost',port='3306', user='root', password='root', databaes='pythontest')
            query='create table if not exist user(userId int primary_key, userNamae varchar(200),phone varchar(12))'
            cur = self.con.cursor()
            cur.execute(query)
            print('created')
        
        #insert 
        def insert_user(self, userId, userName, phone):
            query = 'insert into user (userId, userName, phone) values({},'{}','{}'')'.format(userId, userName, phone)
            print (query)
            cur = self.con.cursor()
            cur.execute(query)
            cur.commit()
            
            print('user saved to DB')
        ##fetch data
        def fetch_data(self):
            query= 'select * from user'
            cur = self.con.cursor()
            cur.execute(query)
            for in in cur:
                print('userID:', i[0])
                print('userName:', i[1)
                print('phone:', i[2)
                

                


        


 ##creating object of class
 id=int(input("enter your id "))
 name=input("enter your name")
 phone=input("enter your phone number")
 helper = DV()
 helper.insert_user(id, name,phone)
 helper.fetch_data()







