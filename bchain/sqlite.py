import sqlite3

class db:

     def db_test(self):
        conn = sqlite3.connect('pandemex_db')
        print(conn)


