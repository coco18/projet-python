import sqlite3
from model.activity import Activity
from model.place import Place
from model.equipment import Equipment

class Db:
    """docstring for data base"""
    def __init__(self):
        self.con = sqlite3.connect("db/data.db")

    def create_table(self):
        cur = self.con.cursor()
        cur.execute("DROP TABLE IF EXISTS place")
        cur.execute("CREATE TABLE place(id integer PRIMARY KEY, name_place text, num_street integer, street text, place_says text, city text, city_code integer, longitude integer, latitude integer)")
        cur.execute("DROP TABLE IF EXISTS equipment")
        cur.execute("CREATE TABLE equipment(id integer PRIMARY KEY, name_equipment text, num_place integer, FOREIGN KEY(num_place) REFERENCES place(id))")
        cur.execute("DROP TABLE IF EXISTS activity")
        cur.execute("CREATE TABLE activity(id integer PRIMARY KEY, name_activity text, level_activity text)")
        cur.execute("DROP TABLE IF EXISTS equipmentactivity")
        cur.execute("CREATE TABLE equipmentactivity(id_equipment integer, id_activity integer, PRIMARY KEY (id_equipment,id_activity), FOREIGN KEY(id_equipment) REFERENCES equipment(id), FOREIGN KEY(id_activity) REFERENCES activity(id))")


    def search(self,table,genre,texte): #mettre texte entre "''"
        c = self.con.cursor()
        query =  "SELECT * FROM {0} where {1} LIKE {2}".format(table, genre, texte)
        c.execute(query)
        return c.fetchall()

    def searchcity(self,activity,equipment):
        c = self.con.cursor()
        query = "SELECT * from place where id in (SELECT num_place from equipment where name_equipment= {1} and id IN (SELECT id_equipment from equipmentactivity where id_activity in (SELECT id FROM activity  where name_activity = {0})))".format(activity,equipment)
        c.execute(query)
        return c.fetchall()

    def displaytable(self,table):
        c = self.con.cursor()
        query =  "SELECT * FROM {0} ".format(table)
        c.execute(query)
        return c.fetchall()


    def commit(self):
        self.con.commit()

    def deconnect(self):
        self.con.close()
