import sqlite3

class Db    :
    """docstring for data base"""
    def __init__(self):
        self.con = squlite3

    def connect(self):
        self.con.connect("data.db")

    def cretate_table():
        cur = con.cursor()
        cur.execute("create table activity(id, name_activity, id_equipement, city, num_city)")
        cur.execute("create table place()")

    def deconnect(self):
        self.con.close()
