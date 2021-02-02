import mysql.connector, os

conn = mysql.connector.connect(
    user=os.environ['DB_USER'], 
    password=os.environ['DB_PASSWORD'],
    host=os.environ['DB_HOST'],
    database=os.environ['DB_NAME']
)
conn.autocommit = True

"""
    How to use: 
    from db import Db
    
    # Select
    Db('select').select('select * from users')

    # Delete/Update/Insert
    Db('change').select('delete from users where id = 10')
"""

class Db():

    def __init__(self,action):
        self.action = action

    # Select
    def select(self,q):
        try:
            cursor = conn.cursor()
            cursor.execute(q)
            res = cursor.fetchall()
            return str(res)
        except mysql.connector.Error as e:
            return {
                'code'    : 500,
                'message' : str(e)
            }
        
        cursor.close()
        conn.close()
    
    # Insert | Delete | Update
    def change(self,q):
        try:

            cursor = conn.cursor()
            cursor.execute(q)
            return {
                'code'    : 200
            }
            
        except mysql.connector.Error as e:
            return {
                'code'    : 500,
                'message' : str(e)
            }

        cursor.close()
        conn.close()